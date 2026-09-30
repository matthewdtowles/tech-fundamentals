"""
Given the head of a singly linked list, reverse the list and return the new head.

Example 1: 1 -> 2 -> 3 -> 4 -> 5  ->  5 -> 4 -> 3 -> 2 -> 1
Example 2: 1 -> 2                 ->  2 -> 1
Example 3: (empty)                ->  (empty)

Constraints: 0 <= nodes <= 5000. Goal: iterative, O(1) extra space.
Follow-up: also write it recursively and explain its space cost.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


def build(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class TestReverseList(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(to_list(Solution().reverseList(build([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])
        self.assertEqual(to_list(Solution().reverseList(build([1, 2]))), [2, 1])

    def test_empty(self):
        self.assertIsNone(Solution().reverseList(None))

    def test_single(self):
        self.assertEqual(to_list(Solution().reverseList(build([7]))), [7])

    def test_reuses_nodes(self):
        head = build([1, 2, 3])
        nodes = [head, head.next, head.next.next]
        new_head = Solution().reverseList(head)
        self.assertIs(new_head, nodes[2])
        self.assertIsNone(nodes[0].next)

    def test_long_list(self):
        self.assertEqual(to_list(Solution().reverseList(build(range(5000)))), list(range(4999, -1, -1)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
