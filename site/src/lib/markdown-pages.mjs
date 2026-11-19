// The Markdown version of each content page (sessions, readings, overview pages), plus llms.txt and
// llms-full.txt. Used by the .md and .txt endpoints, by PageTitle (to know whether a page has a
// Markdown version) and by scripts/check-markdown-pages.mjs. Plain ESM; reads course/ from disk.
import fs from 'node:fs';
import path from 'node:path';
import { parse as parseYaml } from 'yaml';
import { COURSE_DIR, readReadings, readModules, licenseLabel, KIND_LABELS } from './course.mjs';

/** Overview pages, in course order. Only those whose file exists in course/ get a Markdown version.
 *  The title is the frontmatter title if the file has one, otherwise the name below. */
const OVERVIEW = [
  { name: 'start-here', title: 'Start here' },
  { name: 'primer', title: 'Primer' },
  { name: 'curriculum', title: 'Curriculum' },
];
const READING_GROUPS = [
  { prefix: 'A', label: 'Anthropic engineering posts' },
  { prefix: 'B', label: 'Other posts' },
  { prefix: 'P', label: 'Papers' },
  { prefix: 'R', label: 'Repositories' },
];

// ---------------------------------------------------------------------------------------------
// Which pages exist

/** Split a Markdown source into its YAML frontmatter (parsed) and the body. */
export function splitFrontmatter(text) {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---[ \t]*(?:\r?\n|$)/);
  if (!m) return { data: {}, body: text };
  return { data: parseYaml(m[1]) ?? {}, body: text.slice(m[0].length) };
}

function readSource(rel) {
  return splitFrontmatter(fs.readFileSync(path.join(COURSE_DIR, rel), 'utf8').replace(/\r\n/g, '\n'));
}

const keyOrder = (k) => 'ABPR'.indexOf(k[0]) * 1000 + Number(k.slice(1));

function overviewPages() {
  return OVERVIEW.filter((o) => fs.existsSync(path.join(COURSE_DIR, `${o.name}.md`))).map((o) => ({
    kind: 'overview',
    name: o.name,
    source: `${o.name}.md`,
    defaultTitle: o.title,
    htmlPath: `/${o.name}/`,
    mdPath: `/${o.name}.md`,
  }));
}

function sessionFiles() {
  return fs
    .readdirSync(path.join(COURSE_DIR, 'sessions'))
    .filter((f) => f.endsWith('.md'))
    .map((f) => f.replace(/\.md$/, ''));
}

function sessionPages() {
  return sessionFiles()
    .map((slug) => {
      const { data } = readSource(`sessions/${slug}.md`);
      return {
        kind: 'session',
        slug,
        id: String(data.id ?? ''),
        order: Number(data.order ?? 0),
        source: `sessions/${slug}.md`,
        htmlPath: `/sessions/${slug}/`,
        mdPath: `/sessions/${slug}.md`,
      };
    })
    .sort((a, b) => a.order - b.order);
}

function readingPages() {
  return readReadings()
    .sort((a, b) => keyOrder(a.key) - keyOrder(b.key))
    .map((r) => ({
      kind: 'reading',
      key: r.key,
      reading: r,
      source: `readings/${r.key}.md`,
      htmlPath: `/readings/${r.key}/`,
      mdPath: `/readings/${r.key}.md`,
    }));
}

/** Every page with a Markdown version, in course order: overview pages, sessions, readings by key. */
export function markdownPages() {
  return [...overviewPages(), ...sessionPages(), ...readingPages()];
}
export { overviewPages, sessionPages, readingPages };

/** The Markdown URL path for a page's URL path ("/sessions/s01-x/" -> "/sessions/s01-x.md"), or
 *  null when the page has none. Cheap: no file is parsed. */
export function markdownPathFor(pathname) {
  let p = decodeURI(pathname || '/')
    .replace(/\/index\.html$/, '/')
    .replace(/\.html$/, '')
    .replace(/\/+$/, '');
  let m;
  if ((m = p.match(/^\/sessions\/([^/]+)$/))) {
    return sessionFiles().includes(m[1]) ? `/sessions/${m[1]}.md` : null;
  }
  if ((m = p.match(/^\/readings\/([ABPR]\d{1,2})$/))) {
    return readReadings().some((r) => r.key === m[1]) ? `/readings/${m[1]}.md` : null;
  }
  if ((m = p.match(/^\/([a-z-]+)$/))) {
    return overviewPages().find((o) => o.name === m[1])?.mdPath ?? null;
  }
  return null;
}

// ---------------------------------------------------------------------------------------------
// Rewriting a course Markdown body

/** The course text license, as course/LICENSE states it, e.g. "CC BY 4.0". */
export function courseLicense() {
  const text = fs.readFileSync(path.join(COURSE_DIR, 'LICENSE'), 'utf8');
  const m = text.match(/\((CC[ -]BY[^)]*)\)/);
  if (!m) throw new Error('course/LICENSE: could not find the license name, e.g. "(CC BY 4.0)"');
  return m[1];
}

/** github-slugger's slug, which Astro uses for heading ids: lowercase, drop punctuation and symbols,
 *  spaces to hyphens. */
function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^\p{L}\p{M}\p{Nd}\p{Nl}\p{Pc} -]/gu, '')
    .replace(/ /g, '-');
}
class Slugger {
  seen = new Map();
  slug(text) {
    const base = slugify(text);
    let s = base;
    while (this.seen.has(s)) {
      const n = this.seen.get(base) + 1;
      this.seen.set(base, n);
      s = `${base}-${n}`;
    }
    this.seen.set(s, 0);
    return s;
  }
}

/** The text of a heading's inline Markdown, as it is rendered (no markup, link text only). */
function headingText(md) {
  return md
    .replace(/!\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/\[([^\]]*)\]\[[^\]]*\]/g, '$1')
    .replace(/<[^>]+>/g, '')
    .replace(/(`+)(.*?)\1/g, '$2')
    .replace(/(\*\*|__)(.+?)\1/g, '$2')
    .replace(/(\*|_)(.+?)\1/g, '$2')
    .replace(/\\([\\`*_{}[\]()#+\-.!])/g, '$1')
    .trim();
}

const FENCE_OPEN = /^(\s*)(`{3,}|~{3,})(.*)$/;
const ATX = /^ {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*$/;
const DETAILS_OPEN = /<details(?:\s[^>]*)?>/i;
const DETAILS_CLOSE = /<\/details\s*>/i;
const ANSWER_SUMMARY = /^\s*<summary>\s*Answer\s*<\/summary>\s*/;

/** Map a link target in course file `sourceRel` to the absolute URL of its Markdown version, or
 *  return it unchanged when it is not a link to another course page. */
export function courseUrl(url, sourceRel, origin) {
  if (/^[a-z][a-z0-9+.-]*:/i.test(url) || url.startsWith('#') || url.startsWith('//')) return url;
  if (url.startsWith('/')) return origin + url;
  const hashAt = url.search(/[#?]/);
  const target = hashAt === -1 ? url : url.slice(0, hashAt);
  const hash = hashAt === -1 ? '' : url.slice(hashAt);
  const resolved = path.posix.normalize(path.posix.join(path.posix.dirname(sourceRel), target));
  const lenient = target.replace(/^(?:\.\.?\/)+/, '');
  const overview = OVERVIEW.map((o) => o.name).join('|');
  for (const p of [resolved, lenient]) {
    let m;
    if ((m = p.match(/^sessions\/([^/]+)\.md$/))) return `${origin}/sessions/${m[1]}.md${hash}`;
    if ((m = p.match(/^readings\/([ABPR]\d{1,2})\.md$/))) return `${origin}/readings/${m[1]}.md${hash}`;
    if (/^readings\.(tsv|bib)$/.test(p)) return `${origin}/readings/`;
    if ((m = p.match(new RegExp(`^(${overview})\\.md$`)))) return `${origin}/${m[1]}.md${hash}`;
  }
  return url;
}

/** Rewrite link targets in one line of Markdown, leaving inline code spans alone. */
function rewriteLinks(line, map) {
  const out = [];
  const code = /(`+)[\s\S]*?[^`]\1(?!`)/g;
  let last = 0;
  let m;
  const prose = (s) =>
    s
      .replace(/(\]\(\s*)<([^>]*)>/g, (_, pre, u) => `${pre}<${map(u)}>`)
      .replace(/(\]\(\s*)([^\s)<>]+)/g, (_, pre, u) => pre + map(u))
      .replace(/^(\s{0,3}\[[^\]]+\]:\s*)(\S+)/, (_, pre, u) => pre + map(u))
      .replace(/(\shref=")([^"]*)(")/gi, (_, pre, u, post) => pre + map(u) + post);
  while ((m = code.exec(line))) {
    out.push(prose(line.slice(last, m.index)), m[0]);
    last = m.index + m[0].length;
  }
  out.push(prose(line.slice(last)));
  return out.join('');
}

/**
 * Turn a course Markdown body (frontmatter already removed) into the body of its Markdown page:
 * - drops a leading "# " heading (the page title replaces it);
 * - rewrites relative links between course files to absolute URLs of their .md versions;
 * - replaces each <details> block whose summary is exactly "Answer" with one line pointing at the
 *   answer on the HTML page, anchored at the nearest preceding heading.
 * Nothing inside fenced code is changed. Headings are slugged as Astro does, to match the page's ids.
 */
export function rewriteBody(body, { sourceRel, origin, pageUrl }) {
  const lines = body.replace(/\r\n/g, '\n').split('\n');
  // Drop the leading H1 (ATX or setext), as remark-course-links does for the HTML page.
  const first = lines.findIndex((l) => l.trim() !== '');
  if (first !== -1) {
    if (/^ {0,3}#[ \t]/.test(lines[first]) || /^ {0,3}#$/.test(lines[first])) lines.splice(first, 1);
    else if (/^ {0,3}=+[ \t]*$/.test(lines[first + 1] ?? '')) lines.splice(first, 2);
  }

  const map = (u) => courseUrl(u, sourceRel, origin);
  const slugger = new Slugger();
  const out = [];
  let fence = null; // { char, len } while inside fenced code
  let lastSlug = '';

  // Returns the fence state after `line`, and whether the line is a heading (sets lastSlug).
  const track = (line) => {
    if (fence) {
      const close = line.match(/^\s*(`{3,}|~{3,})\s*$/);
      if (close && close[1][0] === fence.char && close[1].length >= fence.len) fence = null;
      return true; // fenced (including the closing line)
    }
    const open = line.match(FENCE_OPEN);
    if (open && !(open[2][0] === '`' && open[3].includes('`'))) {
      fence = { char: open[2][0], len: open[2].length };
      return true;
    }
    const h = line.match(ATX);
    if (h) lastSlug = slugger.slug(headingText(h[2] ?? ''));
    return false;
  };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (track(line)) {
      out.push(line);
      continue;
    }
    const open = line.match(DETAILS_OPEN);
    if (open && isAnswerBlock(lines, i, open)) {
      // Find the matching </details>, counting nested <details> and skipping fenced code.
      const anchor = lastSlug;
      const indent = line.match(/^\s*/)[0];
      let depth = 0;
      let j = i;
      let after = '';
      let rest = line.slice(open.index);
      for (;;) {
        if (j !== i && track(lines[j])) {
          j++;
          if (j >= lines.length) break;
          rest = lines[j];
          continue;
        }
        let closed = false;
        const re = /<details(?:\s[^>]*)?>|<\/details\s*>/gi;
        let t;
        while ((t = re.exec(rest))) {
          depth += t[0][1] === '/' ? -1 : 1;
          if (depth === 0) {
            after = rest.slice(t.index + t[0].length);
            closed = true;
            break;
          }
        }
        if (closed) break;
        j++;
        if (j >= lines.length) {
          console.warn(`[markdown-pages] ${sourceRel}: <details> Answer block is not closed; dropped to the end`);
          break;
        }
        rest = lines[j];
      }
      const before = line.slice(0, open.index);
      if (before.trim()) out.push(before.trimEnd());
      out.push(`${indent}Answer: on the page, ${pageUrl}${anchor ? `#${anchor}` : ''}`);
      if (after.trim()) out.push(rewriteLinks(indent + after.trim(), map));
      i = j;
      continue;
    }
    out.push(rewriteLinks(line, map));
  }
  return out.join('\n').replace(/\n{3,}/g, '\n\n').trim();
}

/** Whether the <details> opened on lines[i] has <summary>Answer</summary> as its first content. */
function isAnswerBlock(lines, i, open) {
  let rest = lines[i].slice(open.index + open[0].length);
  for (let j = i; j < lines.length && j < i + 4; j++) {
    if (j > i) rest = lines[j];
    if (rest.trim() === '') continue;
    return ANSWER_SUMMARY.test(rest);
  }
  return false;
}

// ---------------------------------------------------------------------------------------------
// Rendering pages

function readingIndex() {
  return Object.fromEntries(readReadings().map((r) => [r.key, r]));
}

function moduleLabel(id) {
  const mod = readModules().find((m) => m.id === id);
  return mod ? `${mod.id}. ${mod.title}` : String(id ?? '');
}

function readingList(keys, readings, origin) {
  return keys
    .map((k) => `[${k}. ${readings[k]?.title ?? k}](${origin}/readings/${k}.md)`)
    .join('; ');
}

/** The page's title as the site shows it. */
export function pageTitle(page) {
  if (page.kind === 'session') {
    const { data } = readSource(page.source);
    return `${data.id}. ${data.title}`;
  }
  if (page.kind === 'reading') return `${page.reading.key}. ${page.reading.title}`;
  const { data } = readSource(page.source);
  return typeof data.title === 'string' && data.title ? data.title : page.defaultTitle;
}

/** The full Markdown version of one page. `origin` is the site URL without a trailing slash. */
export function renderMarkdownPage(page, origin) {
  const pageUrl = origin + page.htmlPath;
  const head = [`# ${pageTitle(page)}`];

  if (page.kind === 'session') {
    const { data } = readSource(page.source);
    const readings = readingIndex();
    const reads = data.reads ?? [];
    const optional = data.optional ?? [];
    head.push(`Module: ${moduleLabel(data.module)}`);
    head.push(
      reads.length
        ? `Readings: ${readingList(reads, readings, origin)}`
        : 'Readings: none. Your trajectories, logs or code are the reading.',
    );
    if (optional.length) head.push(`Optional: ${readingList(optional, readings, origin)}`);
  } else if (page.kind === 'reading') {
    const r = page.reading;
    head.push(`${r.authors}${r.year ? `, ${r.year}` : ''}. ${KIND_LABELS[r.kind] ?? r.kind}.`);
    const items =
      r.kind === 'arxiv'
        ? [`- arXiv: https://arxiv.org/abs/${r.source}`, `- PDF: https://arxiv.org/pdf/${r.source}`]
        : [`- Source: ${r.source}`];
    items.push(`- License: ${licenseLabel(r.license)}`);
    if (r.bibkey) items.push(`- BibTeX key: \`${r.bibkey}\``);
    head.push(items.join('\n'));
  }

  const file = path.join(COURSE_DIR, page.source);
  const body = fs.existsSync(file)
    ? rewriteBody(readSource(page.source).body, { sourceRel: page.source, origin, pageUrl })
    : '';
  const tail = `Source: ${pageUrl}. Course text is licensed ${courseLicense()}.`;
  return [...head, ...(body ? [body] : []), tail].join('\n\n') + '\n';
}

// ---------------------------------------------------------------------------------------------
// llms.txt and llms-full.txt

export function renderLlmsTxt(origin) {
  const overview = overviewPages();
  const sessions = sessionPages();
  const readings = readingPages();
  const byId = Object.fromEntries(sessions.map((s) => [s.id, s]));
  const link = (p) => `[${pageTitle(p)}](${origin}${p.mdPath})`;
  const out = [
    '# Agent Harness 101',
    `> A course in agent harness engineering, learned by building one. You start with a deliberately naive coding agent, about a hundred lines with a single bash tool, and grow it one component at a time over ${sessions.length} sessions: tool design, loop control, context management, planning, subagents, verification, evaluation rigor and harness optimization. Every change is measured against a 12-task eval set, with pass rate and token counts side by side.`,
    'Each session takes 45 to 60 minutes: read one paper, post or section that motivates a component (about 20 minutes), build one change to `harness/agent.py` or the lab tooling (about 30), then run the evals and write a log entry (about 10). Reading keys such as A1 or P10 refer to the reading list; each reading has a guide saying which sections the course needs. The lab runs in your own copy of the template repository, with Claude Code as a tutor that quizzes you on the reading and reviews your changes. Every link below is the Markdown version of a page on the site. Answers to the quiz questions are left out and point to the HTML page.',
    `Course text is licensed ${courseLicense()}. The papers and posts belong to their authors; the reading list records each one's license.`,
  ];
  if (overview.length) out.push('## Overview', overview.map((p) => `- ${link(p)}`).join('\n'));

  out.push('## Sessions');
  const listed = new Set();
  const sessionLine = (s) => {
    const { data } = readSource(s.source);
    const reads = data.reads ?? [];
    const optional = data.optional ?? [];
    let note = reads.length ? `reads ${reads.join(', ')}` : 'no reading; your trajectories, logs or code';
    if (optional.length) note += `; optional ${optional.join(', ')}`;
    return `- ${link(s)}: ${note}`;
  };
  for (const m of readModules()) {
    const items = (m.sessions ?? []).map((id) => byId[id]).filter(Boolean);
    items.forEach((s) => listed.add(s.id));
    out.push(`### ${m.id}. ${m.title}`, items.map(sessionLine).join('\n'));
  }
  const unlisted = sessions.filter((s) => !listed.has(s.id));
  if (unlisted.length) out.push('### Other sessions', unlisted.map(sessionLine).join('\n'));

  out.push('## Readings', `The reading list with authors and years: [Readings](${origin}/readings/).`);
  for (const g of READING_GROUPS) {
    const items = readings.filter((r) => r.key.startsWith(g.prefix));
    if (!items.length) continue;
    out.push(`### ${g.label}`, items.map((r) => `- ${link(r)}: license: ${licenseLabel(r.reading.license)}`).join('\n'));
  }

  out.push('## Optional', `- [The whole course in one file](${origin}/llms-full.txt): every page above, in course order`);
  return out.join('\n\n') + '\n';
}

export function renderLlmsFullTxt(origin, builtAt = new Date()) {
  const pages = markdownPages();
  const header = [
    '# Agent Harness 101: the full course in Markdown',
    `The Markdown version of every page of ${origin}/, in course order: the overview pages, the sessions in order, then the reading guides by key. Pages are separated by a line of three hyphens. Answers to the quiz questions are left out; each one points to its place on the HTML page.`,
    `Built ${builtAt.toISOString()}. Course text is licensed ${courseLicense()}. The papers and posts the readings point to belong to their authors and are not included.`,
  ].join('\n\n');
  return [header, ...pages.map((p) => renderMarkdownPage(p, origin).trim())].join('\n\n---\n\n') + '\n';
}

/** Site origin without a trailing slash, from Astro's `site` (a URL or string). */
export function originFrom(site) {
  if (!site) throw new Error('Set `site` in astro.config.mjs: the Markdown pages need absolute URLs');
  return String(site).replace(/\/+$/, '');
}
