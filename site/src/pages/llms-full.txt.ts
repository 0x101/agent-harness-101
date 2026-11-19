// /llms-full.txt: every Markdown page concatenated in course order.
import type { APIRoute } from 'astro';
import { renderLlmsFullTxt, originFrom } from '../lib/markdown-pages.mjs';

export const GET: APIRoute = ({ site }) =>
  new Response(renderLlmsFullTxt(originFrom(site)), {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
