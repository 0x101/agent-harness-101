// Helpers that read the course files at build time. Plain ESM so astro.config can import it too.
import fs from 'node:fs';
import path from 'node:path';
import { parse as parseYaml } from 'yaml';

/** Locate course/ by walking up from the working directory, so it works from site/ and the repo root,
 *  and from the relocated build chunks under dist/. COURSE_DIR in the environment overrides it. */
function findCourseDir() {
  if (process.env.COURSE_DIR) return path.resolve(process.env.COURSE_DIR) + path.sep;
  let dir = process.cwd();
  for (let i = 0; i < 5; i++) {
    const candidate = path.join(dir, 'course');
    if (fs.existsSync(path.join(candidate, 'readings.tsv'))) return candidate + path.sep;
    dir = path.dirname(dir);
  }
  throw new Error('course/ not found above ' + process.cwd() + '; set COURSE_DIR');
}
export const COURSE_DIR = findCourseDir();

/** Parse a TSV with a header row into an array of objects. */
export function parseTsv(text) {
  const lines = text.split(/\r?\n/).filter((l) => l.length);
  const cols = lines[0].split('\t');
  return lines.slice(1).map((line) => {
    const cells = line.split('\t');
    return Object.fromEntries(cols.map((c, i) => [c, cells[i] ?? '']));
  });
}

export function readReadings() {
  return parseTsv(fs.readFileSync(path.join(COURSE_DIR, 'readings.tsv'), 'utf8'));
}

export function readModules() {
  return parseYaml(fs.readFileSync(path.join(COURSE_DIR, 'modules.yaml'), 'utf8')).modules;
}

/** Minimal frontmatter read for the generated session files: id, title, order, module. */
export function readSessions() {
  const dir = path.join(COURSE_DIR, 'sessions');
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith('.md'))
    .map((f) => {
      const text = fs.readFileSync(path.join(dir, f), 'utf8');
      const fm = text.split('\n---\n')[0];
      const get = (k) => (fm.match(new RegExp(`^${k}: (.*)$`, 'm')) || [])[1] ?? '';
      return {
        slug: f.replace(/\.md$/, ''),
        id: get('id'),
        module: get('module'),
        title: get('title').replace(/^"(.*)"$/, '$1').replace(/\\"/g, '"'),
        order: Number(get('order')),
      };
    })
    .sort((a, b) => a.order - b.order);
}

/** Map of reading key -> BibTeX entry text, split on the "% KEY" marker lines. */
export function readBib() {
  const text = fs.readFileSync(path.join(COURSE_DIR, 'readings.bib'), 'utf8');
  const out = {};
  const re = /^% ([ABPR]\d{1,2})\n([\s\S]*?)(?=\n% [ABPR]\d{1,2}\n|\s*$)/gm;
  let m;
  while ((m = re.exec(text))) out[m[1]] = m[2].trim();
  return out;
}

/** Sidebar groups for Starlight, built from modules.yaml and the session files. */
export function buildSidebar() {
  const sessions = readSessions();
  const byId = Object.fromEntries(sessions.map((s) => [s.id, s]));
  return readModules().map((m) => ({
    label: `${m.id}. ${m.title}`,
    collapsed: m.id !== 'M0',
    items: m.sessions.map((id) => {
      const s = byId[id];
      if (!s) throw new Error(`modules.yaml lists ${id} but no session file has that id`);
      return { label: `${s.id}. ${s.title}`, slug: `sessions/${s.slug}` };
    }),
  }));
}

const LICENSE_LABELS = {
  'CC-BY-4.0': 'CC BY 4.0',
  'CC-BY-NC-SA-4.0': 'CC BY-NC-SA 4.0',
  'arXiv-nonexclusive-1.0': 'arXiv non-exclusive license (no redistribution)',
  copyright: 'All rights reserved',
  'see-repo': 'See the repository',
};
export function licenseLabel(code) {
  return LICENSE_LABELS[code] ?? code;
}
export const KIND_LABELS = { arxiv: 'Paper (arXiv)', web: 'Web post', repo: 'Repository' };
