// /llms.txt in the llmstxt.org layout, pointing at the Markdown version of every page.
import type { APIRoute } from 'astro';
import { renderLlmsTxt, originFrom } from '../lib/markdown-pages.mjs';

export const GET: APIRoute = ({ site }) =>
  new Response(renderLlmsTxt(originFrom(site)), {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
