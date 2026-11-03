import heapq


class CycleError(Exception):
    pass


def build_order(graph):
    nodes = set(graph)
    for deps in graph.values():
        nodes.update(deps)
    indeg = {n: 0 for n in nodes}
    users = {n: [] for n in nodes}
    for n, deps in graph.items():
        for d in set(deps):
            indeg[n] += 1
            users[d].append(n)
    ready = [n for n in nodes if indeg[n] == 0]
    heapq.heapify(ready)
    out = []
    while ready:
        n = heapq.heappop(ready)
        out.append(n)
        for u in users[n]:
            indeg[u] -= 1
            if indeg[u] == 0:
                heapq.heappush(ready, u)
    if len(out) != len(nodes):
        raise CycleError(sorted(nodes - set(out)))
    return out
