"""
Given the root of a binary tree, determine if it is a valid binary search tree:
  - every node in a node's LEFT subtree has a value strictly LESS than the node
  - every node in its RIGHT subtree has a value strictly GREATER
  - both subtrees are also BSTs

Example 1: [2,1,3]                    ->  True
Example 2: [5,1,4,null,null,3,6]      ->  False  (4 is in 5's right subtree)

Constraints: 1 <= nodes <= 10^4, -2^31 <= val <= 2^31 - 1
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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


class TestValidateBST(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(Solution().isValidBST(build_tree([2, 1, 3])))
        self.assertFalse(Solution().isValidBST(build_tree([5, 1, 4, None, None, 3, 6])))

    def test_violation_deeper_than_parent(self):
        self.assertFalse(Solution().isValidBST(build_tree([5, 4, 6, None, None, 3, 7])))

    def test_duplicates_invalid(self):
        self.assertFalse(Solution().isValidBST(build_tree([1, 1])))
        self.assertFalse(Solution().isValidBST(build_tree([1, None, 1])))

    def test_extreme_values(self):
        self.assertTrue(Solution().isValidBST(build_tree([2 ** 31 - 1])))
        self.assertTrue(Solution().isValidBST(build_tree([-(2 ** 31), None, 2 ** 31 - 1])))

    def test_larger_valid(self):
        self.assertTrue(Solution().isValidBST(build_tree([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7])))


if __name__ == "__main__":
    unittest.main(verbosity=2)
