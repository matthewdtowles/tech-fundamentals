"""
Given a reference to a node in a connected undirected graph, return a DEEP copy
(clone) of the graph. Each node has a val (int) and a list of neighbors.

Node values are 1..n and equal their position in the tests' adjacency list, e.g.
adjList = [[2,4],[1,3],[2,4],[1,3]] means node 1's neighbors are 2 and 4, etc.
The given node is always node 1. An empty graph is None.

Constraints: 0 <= n <= 100, no repeated edges, no self-loops. Graph may have cycles.
"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


def build_graph(adj):
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for node, neighbors in zip(nodes, adj):
        node.neighbors = [nodes[v - 1] for v in neighbors]
    return nodes[0]


def collect(start):
    seen, stack = {}, [start]
    while stack:
        node = stack.pop()
        if node.val not in seen:
            seen[node.val] = node
            stack.extend(node.neighbors)
    return seen


def to_adj(start):
    nodes = collect(start)
    return [[n.val for n in nodes[v].neighbors] for v in sorted(nodes)]


class TestCloneGraph(unittest.TestCase):
    def check(self, adj):
        original = build_graph(adj)
        clone = Solution().cloneGraph(original)
        self.assertEqual(to_adj(clone), adj)
        originals = {id(n) for n in collect(original).values()}
        self.assertTrue(all(id(n) not in originals for n in collect(clone).values()), "clone shares nodes with original")

    def test_square_cycle(self):
        self.check([[2, 4], [1, 3], [2, 4], [1, 3]])

    def test_single_node(self):
        self.check([[]])

    def test_empty(self):
        self.assertIsNone(Solution().cloneGraph(None))

    def test_complete_graph(self):
        n = 6
        self.check([[j + 1 for j in range(n) if j != i] for i in range(n)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
