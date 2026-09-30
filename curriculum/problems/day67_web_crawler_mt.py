"""
Given startUrl and an HtmlParser, crawl every URL reachable from startUrl that
has the SAME hostname as startUrl, using multiple threads. Return them in any order.

  HtmlParser.getUrls(url) -> list of URLs linked from url   (slow: network I/O!)

URLs look like "http://news.yahoo.com/news/topics/"; the hostname is
"news.yahoo.com". Assume http only, no ports. The same URL must not be fetched
twice. URLs with and without a trailing slash are different URLs.

The tests' parser sleeps 50 ms per call: a single-threaded crawl of 40 pages
takes ~2 s; yours must finish in under 1 s.

Discuss first: ThreadPoolExecutor and futures, why check-then-add on the visited
set must be atomic, how you know the crawl is finished, why threads help
I/O-bound work despite the GIL.
"""
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List


class HtmlParser:
    def getUrls(self, url: str) -> List[str]:
        ...


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class FakeParser:
    def __init__(self, graph, delay=0.05):
        self.graph, self.delay = graph, delay
        self.calls, self.lock = [], threading.Lock()

    def getUrls(self, url):
        with self.lock:
            self.calls.append(url)
        time.sleep(self.delay)
        return list(self.graph.get(url, []))


class TestCrawler(unittest.TestCase):
    def test_example(self):
        graph = {
            "http://news.yahoo.com/news/topics/": ["http://news.yahoo.com", "http://news.yahoo.com/news"],
            "http://news.yahoo.com": ["http://news.google.com", "http://news.yahoo.com/us"],
            "http://news.yahoo.com/news": ["http://news.yahoo.com/news/topics/"],
            "http://news.google.com": ["http://news.yahoo.com/other"],
        }
        parser = FakeParser(graph, delay=0)
        got = Solution().crawl("http://news.yahoo.com/news/topics/", parser)
        self.assertEqual(sorted(got), sorted([
            "http://news.yahoo.com/news/topics/", "http://news.yahoo.com",
            "http://news.yahoo.com/news", "http://news.yahoo.com/us",
        ]))
        self.assertNotIn("http://news.google.com", parser.calls, "don't fetch other hosts")

    def test_no_duplicate_fetches(self):
        hub = "http://a.com/hub"
        graph = {hub: [f"http://a.com/{i}" for i in range(20)]}
        for i in range(20):
            graph[f"http://a.com/{i}"] = [hub] + [f"http://a.com/{j}" for j in range(20)]
        parser = FakeParser(graph, delay=0.01)
        got = Solution().crawl(hub, parser)
        self.assertEqual(len(got), 21)
        self.assertEqual(len(parser.calls), len(set(parser.calls)), "a URL was fetched twice (visited race)")

    def test_concurrent_speedup(self):
        graph = {"http://site.org/0": [f"http://site.org/{i}" for i in range(1, 40)]}
        parser = FakeParser(graph, delay=0.05)
        start = time.perf_counter()
        got = Solution().crawl("http://site.org/0", parser)
        self.assertEqual(len(got), 40)
        self.assertLess(time.perf_counter() - start, 1.0, "fetches are not running concurrently")


if __name__ == "__main__":
    unittest.main(verbosity=2)
