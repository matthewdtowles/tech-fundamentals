"""
Given a string s containing only '(', ')', '{', '}', '[' and ']', return True if
it is valid: every opener is closed by the same type, in the correct order, and
every closer has a matching opener.

Example 1: "()"      -> True
Example 2: "()[]{}"  -> True
Example 3: "(]"      -> False
Example 4: "([])"    -> True

Constraints: 1 <= len(s) <= 10^4
"""


class Solution:
    def isValid(self, s: str) -> bool:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestIsValid(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(Solution().isValid("()"))
        self.assertTrue(Solution().isValid("()[]{}"))
        self.assertFalse(Solution().isValid("(]"))
        self.assertTrue(Solution().isValid("([])"))

    def test_wrong_order(self):
        self.assertFalse(Solution().isValid("([)]"))

    def test_unclosed(self):
        self.assertFalse(Solution().isValid("(("))

    def test_closer_first(self):
        self.assertFalse(Solution().isValid("]"))
        self.assertFalse(Solution().isValid("){"))

    def test_deep_nesting(self):
        self.assertTrue(Solution().isValid("{[(" * 3000 + ")]}" * 3000))


if __name__ == "__main__":
    unittest.main(verbosity=2)
