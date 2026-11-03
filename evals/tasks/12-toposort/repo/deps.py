class CycleError(Exception):
    pass


def build_order(graph):
    """Return a build order for a dependency graph.

    graph maps each node to the list of nodes it depends on. Nodes that only
    appear as dependencies are still part of the graph.

    - Every dependency comes before the nodes that depend on it.
    - When several nodes are ready at once, take them in alphabetical order.
      So {"b": [], "a": []} -> ["a", "b"].
    - Raise CycleError if the graph has a cycle.
    """
    raise NotImplementedError
