"""
Decode an encoded string. The rule is k[encoded_string]: the encoded_string
inside the brackets is repeated exactly k times (k is a positive integer, may be
multi-digit). Input is always valid; digits only appear as repeat counts.

Example 1: "3[a]2[bc]"      -> "aaabcbc"
Example 2: "3[a2[c]]"       -> "accaccacc"
Example 3: "2[abc]3[cd]ef"  -> "abcabccdcdcdef"

Constraints: 1 <= len(s) <= 30, output length <= 10^5
"""


class Solution:
    def decodeString(self, s: str) -> str:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestDecodeString(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().decodeString("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(Solution().decodeString("3[a2[c]]"), "accaccacc")
        self.assertEqual(Solution().decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_multi_digit(self):
        self.assertEqual(Solution().decodeString("10[a]"), "a" * 10)
        self.assertEqual(Solution().decodeString("12[xy]z"), "xy" * 12 + "z")

    def test_plain(self):
        self.assertEqual(Solution().decodeString("abc"), "abc")

    def test_prefix_and_nesting(self):
        self.assertEqual(Solution().decodeString("ab2[c3[d]]e"), "abcdddcddde")


if __name__ == "__main__":
    unittest.main(verbosity=2)
