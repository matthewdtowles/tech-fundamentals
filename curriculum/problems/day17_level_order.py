"""
Given the root of a binary tree, return the level order traversal of its node
values: left to right, level by level, as a list of lists.

Example 1: [3,9,20,null,null,15,7]  ->  [[3],[9,20],[15,7]]
Example 2: [1]                      ->  [[1]]
Example 3: []                       ->  []

Constraints: 0 <= nodes <= 2000
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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


class TestLevelOrder(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().levelOrder(build_tree([3, 9, 20, None, None, 15, 7])), [[3], [9, 20], [15, 7]])
        self.assertEqual(Solution().levelOrder(build_tree([1])), [[1]])
        self.assertEqual(Solution().levelOrder(None), [])

    def test_uneven(self):
        self.assertEqual(Solution().levelOrder(build_tree([1, 2, 3, 4, None, None, 5])), [[1], [2, 3], [4, 5]])

    def test_skewed(self):
        self.assertEqual(Solution().levelOrder(build_tree([1, None, 2, None, 3])), [[1], [2], [3]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
