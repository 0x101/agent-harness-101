// The Markdown version of each reading page: /readings/<KEY>.md
import type { APIRoute } from 'astro';
import { readingPages, renderMarkdownPage, originFrom } from '../../lib/markdown-pages.mjs';

export function getStaticPaths() {
  return readingPages().map((page) => ({ params: { key: page.key }, props: { page } }));
}

export const GET: APIRoute = ({ props, site }) =>
  new Response(renderMarkdownPage(props.page, originFrom(site)), {
    headers: { 'Content-Type': 'text/markdown; charset=utf-8' },
  });
