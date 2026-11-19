// The Markdown version of the overview pages that exist in course/ (curriculum.md, and start-here.md
// and primer.md when present): /<name>.md
import type { APIRoute } from 'astro';
import { overviewPages, renderMarkdownPage, originFrom } from '../lib/markdown-pages.mjs';

export function getStaticPaths() {
  return overviewPages().map((page) => ({ params: { overview: page.name }, props: { page } }));
}

export const GET: APIRoute = ({ props, site }) =>
  new Response(renderMarkdownPage(props.page, originFrom(site)), {
    headers: { 'Content-Type': 'text/markdown; charset=utf-8' },
  });
