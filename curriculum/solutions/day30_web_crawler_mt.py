import threading
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from typing import List


class HtmlParser:
    def getUrls(self, url: str) -> List[str]:
        ...


def hostname(url):
    return url.split("/")[2]


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        host = hostname(startUrl)
        visited = {startUrl}
        lock = threading.Lock()

        def fetch(url):
            fresh = []
            for link in htmlParser.getUrls(url):
                if hostname(link) != host:
                    continue
                with lock:  # check-and-add must be one atomic step
                    if link in visited:
                        continue
                    visited.add(link)
                fresh.append(link)
            return fresh

        with ThreadPoolExecutor(max_workers=16) as pool:
            pending = {pool.submit(fetch, startUrl)}
            while pending:  # finished when no fetch is in flight
                done, pending = wait(pending, return_when=FIRST_COMPLETED)
                for future in done:
                    pending |= {pool.submit(fetch, url) for url in future.result()}
        return list(visited)
