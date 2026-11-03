// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { unified } from '@astrojs/markdown-remark';
import { buildSidebar, readReadings } from './src/lib/course.mjs';
import remarkCitations from './src/plugins/remark-citations.mjs';
import remarkCourseLinks from './src/plugins/remark-course-links.mjs';

const readingKeys = readReadings().map((r) => r.key);

export default defineConfig({
  site: 'https://agent-harness-101.example',
  markdown: {
    // Astro 7 defaults to the Sätteri processor; the course needs remark plugins, so use unified.
    processor: unified({
      remarkPlugins: [remarkCourseLinks, [remarkCitations, { keys: readingKeys }]],
    }),
  },
  vite: { server: { fs: { allow: ['..'] } } },
  integrations: [
    starlight({
      title: 'Agent Harness 101',
      description:
        'Learn agent harness engineering by growing a naive coding agent, one measured change at a time.',
      components: { PageTitle: './src/components/PageTitle.astro' },
      sidebar: [
        { label: 'Curriculum', link: '/curriculum/' },
        ...buildSidebar(),
        { label: 'Readings', link: '/readings/' },
        { label: 'Lab', link: '/lab/' },
      ],
    }),
  ],
});
