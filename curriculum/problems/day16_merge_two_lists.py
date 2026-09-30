"""
Merge two sorted linked lists into one sorted list by SPLICING the existing
nodes together (don't allocate new value nodes). Return the head.

Example 1: 1->2->4 and 1->3->4  ->  1->1->2->3->4->4
Example 2: (empty) and (empty)   ->  (empty)
Example 3: (empty) and 0         ->  0

Constraints: 0 <= nodes per list <= 50, values in [-100, 100]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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


def all_nodes(head):
    out = []
    while head:
        out.append(head)
        head = head.next
    return out


class TestMergeTwoLists(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(to_list(Solution().mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))), [1, 1, 2, 3, 4, 4])
        self.assertIsNone(Solution().mergeTwoLists(None, None))
        self.assertEqual(to_list(Solution().mergeTwoLists(None, build([0]))), [0])

    def test_uneven(self):
        self.assertEqual(to_list(Solution().mergeTwoLists(build([5]), build([1, 2, 3, 6, 7]))), [1, 2, 3, 5, 6, 7])

    def test_negatives(self):
        self.assertEqual(to_list(Solution().mergeTwoLists(build([-3, 0]), build([-5, -1]))), [-5, -3, -1, 0])

    def test_splices_existing_nodes(self):
        a, b = build([1, 3]), build([2, 4])
        original = {id(n) for n in all_nodes(a) + all_nodes(b)}
        merged = all_nodes(Solution().mergeTwoLists(a, b))
        self.assertEqual({id(n) for n in merged}, original)


if __name__ == "__main__":
    unittest.main(verbosity=2)
