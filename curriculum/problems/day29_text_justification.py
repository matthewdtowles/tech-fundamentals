"""
Given words and a maxWidth, format the text so each line has exactly maxWidth
characters and is fully (left AND right) justified.

Rules:
  - Pack greedily: as many words per line as fit with at least one space between.
  - Distribute extra spaces as evenly as possible between words. If they don't
    divide evenly, the LEFT gaps get more spaces than the right ones.
  - A line with a single word is left-justified (pad right with spaces).
  - The LAST line is left-justified: single spaces between words, pad right.

Example: words = ["This","is","an","example","of","text","justification."], maxWidth = 16
  [
    "This    is    an",
    "example  of text",
    "justification.  "
  ]

Constraints: 1 <= len(word) <= maxWidth <= 100
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import unittest


class TestFullJustify(unittest.TestCase):
    def test_example_1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        self.assertEqual(Solution().fullJustify(words, 16), ["This    is    an", "example  of text", "justification.  "])

    def test_example_2_single_word_line(self):
        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        self.assertEqual(Solution().fullJustify(words, 16), ["What   must   be", "acknowledgment  ", "shall be        "])

    def test_example_3_uneven_gaps(self):
        words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                 "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
        self.assertEqual(Solution().fullJustify(words, 20), [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ])

    def test_exact_fit(self):
        self.assertEqual(Solution().fullJustify(["ab", "cd"], 5), ["ab cd"])

    def test_one_word(self):
        self.assertEqual(Solution().fullJustify(["a"], 3), ["a  "])


if __name__ == "__main__":
    unittest.main(verbosity=2)
