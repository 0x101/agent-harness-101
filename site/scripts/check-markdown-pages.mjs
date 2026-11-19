// Run after `astro build` (npm run check). Checks the Markdown versions of the pages, llms.txt and
// llms-full.txt in dist/. Exits 1 with a list of problems if any check fails.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { markdownPages, sessionPages, originFrom } from '../src/lib/markdown-pages.mjs';

const siteDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const dist = path.join(siteDir, 'dist');
const { default: config } = await import(path.join(siteDir, 'astro.config.mjs'));
const origin = originFrom(config.site);

const problems = [];
const warnings = [];
const fail = (msg) => problems.push(msg);

if (!fs.existsSync(dist)) {
  console.error(`check-markdown-pages: ${dist} does not exist. Run "npm run build" first.`);
  process.exit(1);
}

/** The dist file a site URL path is served from, or null. */
function distFile(urlPath) {
  const p = decodeURIComponent(urlPath.split(/[?#]/)[0]);
  const candidates = p.endsWith('/')
    ? [path.join(dist, p, 'index.html')]
    : [path.join(dist, p), path.join(dist, p, 'index.html'), path.join(dist, `${p}.html`)];
  return candidates.find((f) => fs.existsSync(f) && fs.statSync(f).isFile()) ?? null;
}

/** Text outside fenced code blocks. */
function withoutFences(text) {
  const out = [];
  let fence = null;
  for (const line of text.split('\n')) {
    const m = line.match(/^\s*(`{3,}|~{3,})/);
    if (fence) {
      if (m && m[1][0] === fence[0] && m[1].length >= fence.length && line.trim() === m[1]) fence = null;
      continue;
    }
    if (m) {
      fence = m[1];
      continue;
    }
    out.push(line.replace(/(`+)[\s\S]*?[^`]\1(?!`)/g, ''));
  }
  return out.join('\n');
}

/** Link targets in Markdown prose: inline links, reference definitions and href attributes. */
function linkTargets(text) {
  const prose = withoutFences(text);
  const targets = [];
  for (const m of prose.matchAll(/\]\(\s*<?([^\s)<>]+)>?/g)) targets.push(m[1]);
  for (const m of prose.matchAll(/^\s{0,3}\[[^\]]+\]:\s*<?(\S+?)>?(?:\s|$)/gm)) targets.push(m[1]);
  for (const m of prose.matchAll(/\shref="([^"]*)"/gi)) targets.push(m[1]);
  return targets;
}

const ANSWER = /<summary>\s*Answer\s*<\/summary>/i;
const isRelativeMd = (u) => !/^[a-z][a-z0-9+.-]*:|^\/|^#/i.test(u) && /\.md(?:[#?]|$)/.test(u);
const idCache = new Map();
function htmlIds(file) {
  if (!idCache.has(file)) {
    const html = fs.readFileSync(file, 'utf8');
    idCache.set(file, new Set([...html.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1])));
  }
  return idCache.get(file);
}

// 1. Every page has a non-empty Markdown file, without answers or relative links to course files.
const pages = markdownPages();
let answerPointers = 0;
for (const page of pages) {
  const file = path.join(dist, page.mdPath);
  if (!fs.existsSync(file)) {
    fail(`${page.mdPath}: missing from dist (source ${page.source})`);
    continue;
  }
  const text = fs.readFileSync(file, 'utf8');
  if (!text.trim()) fail(`${page.mdPath}: empty`);
  if (ANSWER.test(withoutFences(text))) fail(`${page.mdPath}: contains <summary>Answer</summary>`);
  for (const u of linkTargets(text)) {
    if (isRelativeMd(u)) fail(`${page.mdPath}: relative link to a course file: ${u}`);
    else if (u.startsWith(origin + '/') && !distFile(u.slice(origin.length)))
      warnings.push(`${page.mdPath}: link to a page that is not in this build: ${u}`);
  }
  // The HTML page exists, and each "Answer: on the page" anchor is an id on it.
  const html = distFile(page.htmlPath);
  if (!html) {
    fail(`${page.mdPath}: the HTML page ${page.htmlPath} is not in dist`);
    continue;
  }
  for (const m of text.matchAll(/^\s*Answer: on the page, (\S+)$/gm)) {
    answerPointers++;
    const url = new URL(m[1]);
    if (url.origin + url.pathname !== origin + page.htmlPath) fail(`${page.mdPath}: answer points at ${m[1]}`);
    const id = decodeURIComponent(url.hash.slice(1));
    if (id && !htmlIds(html).has(id)) fail(`${page.mdPath}: answer anchor #${id} is not an id on ${page.htmlPath}`);
  }
}

// 2. llms.txt: every link to the site resolves to a file in dist, and every page is listed.
const llmsFile = path.join(dist, 'llms.txt');
let llmsLinks = 0;
if (!fs.existsSync(llmsFile)) fail('llms.txt: missing from dist');
else {
  const llms = fs.readFileSync(llmsFile, 'utf8');
  if (!llms.startsWith('# Agent Harness 101\n')) fail('llms.txt: does not start with "# Agent Harness 101"');
  const urls = [...llms.matchAll(/\]\((\S+?)\)/g)].map((m) => m[1]);
  for (const u of urls.filter((u) => u.startsWith(origin + '/'))) {
    llmsLinks++;
    if (!distFile(u.slice(origin.length))) fail(`llms.txt: ${u} does not resolve to a file in dist`);
  }
  for (const page of pages) {
    if (!urls.includes(origin + page.mdPath)) fail(`llms.txt: does not link ${origin + page.mdPath}`);
  }
}

// 3. llms-full.txt: has every session, and no answers.
const fullFile = path.join(dist, 'llms-full.txt');
if (!fs.existsSync(fullFile)) fail('llms-full.txt: missing from dist');
else {
  const full = fs.readFileSync(fullFile, 'utf8');
  for (const s of sessionPages()) {
    if (!s.id || !full.includes(`\n# ${s.id}. `)) fail(`llms-full.txt: session ${s.id || s.slug} is missing`);
  }
  if (ANSWER.test(withoutFences(full))) fail('llms-full.txt: contains <summary>Answer</summary>');
}

for (const w of new Set(warnings)) console.warn(`warning: ${w}`);
if (problems.length) {
  console.error(`check-markdown-pages: ${problems.length} problem(s)`);
  for (const p of problems) console.error(`  - ${p}`);
  process.exit(1);
}
const counts = pages.reduce((acc, p) => ({ ...acc, [p.kind]: (acc[p.kind] ?? 0) + 1 }), {});
console.log(
  `check-markdown-pages: ok. ${pages.length} Markdown pages (${counts.overview ?? 0} overview, ` +
    `${counts.session ?? 0} sessions, ${counts.reading ?? 0} readings), ${answerPointers} answers left out, ` +
    `${llmsLinks} llms.txt links resolve, llms-full.txt has all ${sessionPages().length} sessions.`,
);
