"""Graph - ANTEQUINA (N2 and A2 are the repeated letters)"""
from collections import deque

EDGES = [
    ("A", "N"), ("A", "T"), ("N", "E"), ("N", "Q"), ("T", "U"),
    ("T", "I"), ("E", "Q"), ("E", "N2"), ("Q", "U"), ("U", "I"),
]
VERTICES = ["A", "N", "T", "E", "Q", "U", "I", "N2", "A2"]


class Graph:
    def __init__(self, vertices, edges):
        self.adj = {v: [] for v in vertices}
        self.edges = edges
        for u, v in edges:          # undirected graph
            self.adj[u].append(v)
            self.adj[v].append(u)

    def bfs(self, start):
        visited, order, queue = {start}, [], deque([start])
        while queue:
            v = queue.popleft()
            order.append(v)
            for nb in self.adj[v]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)
        return order

    def dfs(self, start):
        visited, order = set(), []

        def visit(v):
            visited.add(v)
            order.append(v)
            for nb in self.adj[v]:
                if nb not in visited:
                    visit(nb)

        visit(start)
        return order


def run():
    g = Graph(VERTICES, EDGES)
    print("\n=== GRAPH - ANTEQUINA ===")
    print("Edges:", g.edges)
    print("Total edges:", len(g.edges))
    print("Adjacency List:")
    for v, nbs in g.adj.items():
        print(f"  {v}: {', '.join(nbs) if nbs else 'None (isolated)'}")
    print("BFS from A:", " -> ".join(g.bfs("A")))
    print("DFS from A:", " -> ".join(g.dfs("A")))
