// Rewrites the relative links the course files use for each other into site routes,
// and drops a leading H1 because the page chrome already shows the title.
import { visit } from 'unist-util-visit';

export default function remarkCourseLinks() {
  return (tree) => {
    visit(tree, ['link', 'definition'], (node) => {
      const url = node.url || '';
      let m;
      if ((m = url.match(/^(?:\.\.\/)?sessions\/([^/#?]+)\.md(#.*)?$/))) node.url = `/sessions/${m[1]}/${m[2] ?? ''}`;
      else if ((m = url.match(/^(?:\.\.\/)?readings\/([ABPR]\d{1,2})\.md(#.*)?$/))) node.url = `/readings/${m[1]}/${m[2] ?? ''}`;
      else if (/^(?:\.\.\/)?readings\.(tsv|bib)$/.test(url)) node.url = '/readings/';
      else if (/^(?:\.\.\/)?curriculum\.md$/.test(url)) node.url = '/curriculum/';
    });
    const first = tree.children[0];
    if (first && first.type === 'heading' && first.depth === 1) tree.children.shift();
  };
}
