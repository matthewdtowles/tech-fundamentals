"""
Given a binary tree (NOT necessarily a BST) and two nodes p and q in it, return
their lowest common ancestor: the lowest node that has both p and q as
descendants (a node is a descendant of itself).

Example tree: [3,5,1,6,2,0,8,null,null,7,4]
  p = 5, q = 1  ->  3
  p = 5, q = 4  ->  5
Example 2: [1,2], p = 1, q = 2  ->  1

Constraints: 2 <= nodes <= 10^5, all values unique, p != q, both exist.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest
from collections import deque


def build_tree(values):
    """Build from LeetCode level-order list, e.g. [3, 9, 20, None, None, 15, 7]."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue, i = deque([root]), 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def to_values(root):
    out, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            out.append(node.val)
            queue.extend([node.left, node.right])
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


def find(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find(root.left, val) or find(root.right, val)


class TestLCA(unittest.TestCase):
    def lca(self, values, p, q):
        root = build_tree(values)
        return Solution().lowestCommonAncestor(root, find(root, p), find(root, q)).val

    def test_examples(self):
        tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        self.assertEqual(self.lca(tree, 5, 1), 3)
        self.assertEqual(self.lca(tree, 5, 4), 5)
        self.assertEqual(self.lca([1, 2], 1, 2), 1)

    def test_deep_cousins(self):
        tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        self.assertEqual(self.lca(tree, 7, 6), 5)
        self.assertEqual(self.lca(tree, 7, 8), 3)
        self.assertEqual(self.lca(tree, 4, 7), 2)

    def test_returns_node_object(self):
        root = build_tree([3, 5, 1])
        self.assertIs(Solution().lowestCommonAncestor(root, root.left, root.right), root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
