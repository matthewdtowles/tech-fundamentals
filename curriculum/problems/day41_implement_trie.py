"""
Implement a trie (prefix tree).

  Trie()
  insert(word)          insert word
  search(word)          True if word was inserted
  startsWith(prefix)    True if any inserted word starts with prefix

Example:
  insert("apple")
  search("apple")    -> True
  search("app")      -> False
  startsWith("app")  -> True
  insert("app")
  search("app")      -> True

Constraints: 1 <= len(word) <= 2000, lowercase letters, up to 3 * 10^4 calls.
Goal: each operation O(L) where L is the word length.
"""


class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def startsWith(self, prefix: str) -> bool:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestTrie(unittest.TestCase):
    def test_example(self):
        t = Trie()
        t.insert("apple")
        self.assertTrue(t.search("apple"))
        self.assertFalse(t.search("app"))
        self.assertTrue(t.startsWith("app"))
        t.insert("app")
        self.assertTrue(t.search("app"))

    def test_missing(self):
        t = Trie()
        t.insert("cat")
        self.assertFalse(t.search("dog"))
        self.assertFalse(t.startsWith("ca" + "x"))
        self.assertFalse(t.search("cats"))

    def test_whole_word_is_prefix(self):
        t = Trie()
        t.insert("ab")
        self.assertTrue(t.startsWith("ab"))

    def test_performance(self):
        t = Trie()
        words = [f"word{i}" for i in range(20_000)]
        for w in words:
            t.insert(w)
        start = time.perf_counter()
        for i in range(20_000):
            t.startsWith(f"word{i}")
        self.assertLess(time.perf_counter() - start, 1.0, "startsWith must be O(L), not a scan of all words")


if __name__ == "__main__":
    unittest.main(verbosity=2)
