// The Markdown version of each session page: /sessions/<slug>.md
import type { APIRoute } from 'astro';
import { sessionPages, renderMarkdownPage, originFrom } from '../../lib/markdown-pages.mjs';

export function getStaticPaths() {
  return sessionPages().map((page) => ({ params: { slug: page.slug }, props: { page } }));
}

export const GET: APIRoute = ({ props, site }) =>
  new Response(renderMarkdownPage(props.page, originFrom(site)), {
    headers: { 'Content-Type': 'text/markdown; charset=utf-8' },
  });
