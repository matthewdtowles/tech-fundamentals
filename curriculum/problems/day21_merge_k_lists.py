"""
You are given an array of k linked lists, each sorted ascending.
Merge them all into one sorted linked list and return its head.

Example 1: [1->4->5, 1->3->4, 2->6]  ->  1->1->2->3->4->4->5->6
Example 2: []                        ->  (empty)
Example 3: [(empty)]                 ->  (empty)

Constraints: 0 <= k <= 10^4, total nodes N <= 10^4 (perf test uses more)
Goal: O(N log k). Hint: ListNode is not comparable — think about heap tuples.
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
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


class TestMergeKLists(unittest.TestCase):
    def test_example(self):
        lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
        self.assertEqual(to_list(Solution().mergeKLists(lists)), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_empty(self):
        self.assertIsNone(Solution().mergeKLists([]))
        self.assertIsNone(Solution().mergeKLists([None]))

    def test_mixed_empty(self):
        self.assertEqual(to_list(Solution().mergeKLists([None, build([2]), None, build([1, 3])])), [1, 2, 3])

    def test_equal_values_many_lists(self):
        self.assertEqual(to_list(Solution().mergeKLists([build([1, 1]) for _ in range(5)])), [1] * 10)

    def test_performance(self):
        lists = [build(range(i, 100_000, 2_000)) for i in range(2_000)]
        start = time.perf_counter()
        got = to_list(Solution().mergeKLists(lists))
        self.assertLess(time.perf_counter() - start, 2.0, "Too slow: aim for O(N log k)")
        self.assertEqual(got, list(range(100_000)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
