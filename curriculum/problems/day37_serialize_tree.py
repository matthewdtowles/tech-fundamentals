"""
Design an algorithm to serialize a binary tree to a string and deserialize that
string back to the identical tree structure. Any format you like, as long as
deserialize(serialize(tree)) reproduces the tree.

Codec().serialize(root) -> str
Codec().deserialize(data) -> root

Example: [1,2,3,null,null,4,5] round-trips to [1,2,3,null,null,4,5]

Constraints: 0 <= nodes <= 10^4, -1000 <= val <= 1000 (negatives!)
Rules: the string must carry everything — the tests deserialize with a NEW Codec.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        raise NotImplementedError

    def deserialize(self, data: str) -> Optional[TreeNode]:
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


class TestCodec(unittest.TestCase):
    def roundtrip(self, values):
        data = Codec().serialize(build_tree(values))
        self.assertIsInstance(data, str)
        return to_values(Codec().deserialize(data))

    def test_example(self):
        self.assertEqual(self.roundtrip([1, 2, 3, None, None, 4, 5]), [1, 2, 3, None, None, 4, 5])

    def test_empty(self):
        self.assertEqual(self.roundtrip([]), [])

    def test_negative_and_multi_digit(self):
        self.assertEqual(self.roundtrip([-10, 200, -3, None, 1000]), [-10, 200, -3, None, 1000])

    def test_skewed(self):
        values = [1]
        for v in range(2, 300):
            values += [None, v]
        self.assertEqual(self.roundtrip(values), values)

    def test_duplicates(self):
        self.assertEqual(self.roundtrip([1, 1, 1, 1]), [1, 1, 1, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
