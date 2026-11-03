// Links reading keys to their reading page: "[P10 §4.2]", "[A1]", "[P1 p.3]" and bare "P10".
// Only keys present in readings.tsv are linked. Text already inside a link is left alone.
import { visit } from 'unist-util-visit';

export default function remarkCitations({ keys }) {
  const known = new Set(keys);
  const re = /\[([ABPR]\d{1,2})(?:\s[^\]]*)?\]|\b([ABPR]\d{1,2})\b/g;
  return (tree) => {
    visit(tree, ['link', 'linkReference'], (link) => {
      visit(link, 'text', (t) => {
        t.data = { ...(t.data || {}), noCite: true };
      });
    });
    visit(tree, 'text', (node, index, parent) => {
      if (!parent || index == null || node.data?.noCite) return;
      const value = node.value;
      const out = [];
      let last = 0;
      let m;
      re.lastIndex = 0;
      while ((m = re.exec(value))) {
        const key = m[1] ?? m[2];
        if (!known.has(key)) continue;
        if (m.index > last) out.push({ type: 'text', value: value.slice(last, m.index) });
        out.push({
          type: 'link',
          url: `/readings/${key}/`,
          title: null,
          data: { hProperties: { class: 'cite' } },
          children: [{ type: 'text', value: m[0], data: { noCite: true } }],
        });
        last = m.index + m[0].length;
      }
      if (!out.length) return;
      if (last < value.length) out.push({ type: 'text', value: value.slice(last) });
      parent.children.splice(index, 1, ...out);
      return index + out.length;
    });
  };
}
