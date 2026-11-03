import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders';
import { docsSchema } from '@astrojs/starlight/schema';
import { parseTsv } from './lib/course.mjs';

const keepName = ({ entry }: { entry: string }) => entry.replace(/\.md$/, '');

export const collections = {
  // Starlight's docs collection, pointed at the course sessions instead of src/content/docs.
  docs: defineCollection({
    loader: glob({
      base: '../course/sessions',
      pattern: '*.md',
      generateId: ({ entry }) => `sessions/${keepName({ entry })}`,
    }),
    schema: docsSchema({
      extend: z.object({
        // Optional because StarlightPage validates its own frontmatter against this schema too.
        id: z.string().optional(),
        module: z.string().optional(),
        order: z.number().optional(),
        reads: z.array(z.string()).default([]),
        optional: z.array(z.string()).default([]),
        cites: z.array(z.string()).default([]),
      }),
    }),
  }),
  guides: defineCollection({
    loader: glob({ base: '../course/readings', pattern: '*.md', generateId: keepName }),
    schema: z.object({ key: z.string(), title: z.string() }),
  }),
  readings: defineCollection({
    loader: file('../course/readings.tsv', {
      parser: (text) => parseTsv(text).map((r) => ({ id: r.key, ...r })),
    }),
    schema: z.object({
      key: z.string(),
      kind: z.enum(['arxiv', 'web', 'repo']),
      source: z.string(),
      file: z.string(),
      title: z.string(),
      authors: z.string(),
      year: z.string(),
      license: z.string(),
      read: z.string(),
      skip: z.string(),
      bibkey: z.string(),
    }),
  }),
  overview: defineCollection({
    loader: glob({ base: '../course', pattern: 'curriculum.md', generateId: keepName }),
    schema: z.object({}),
  }),
};
