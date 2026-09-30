"""
Given the root of a binary tree, invert it (mirror every left/right pair) and
return its root.

Example 1: [4,2,7,1,3,6,9]  ->  [4,7,2,9,6,3,1]
Example 2: [2,1,3]          ->  [2,3,1]
Example 3: []               ->  []

(Trees are shown in LeetCode level order; the tests build them for you.)
Constraints: 0 <= nodes <= 100
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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


class TestInvertTree(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(to_values(Solution().invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))), [4, 7, 2, 9, 6, 3, 1])
        self.assertEqual(to_values(Solution().invertTree(build_tree([2, 1, 3]))), [2, 3, 1])
        self.assertIsNone(Solution().invertTree(None))

    def test_lopsided(self):
        self.assertEqual(to_values(Solution().invertTree(build_tree([1, 2, None, 3]))), [1, None, 2, None, 3])

    def test_returns_same_root(self):
        root = build_tree([1, 2, 3])
        self.assertIs(Solution().invertTree(root), root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
