from collections import deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {ch: set() for w in words for ch in w}
        indegree = {ch: 0 for ch in graph}
        for first, second in zip(words, words[1:]):
            for a, b in zip(first, second):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break
            else:
                if len(first) > len(second):
                    return ""
        queue = deque(ch for ch in graph if indegree[ch] == 0)
        order = []
        while queue:
            ch = queue.popleft()
            order.append(ch)
            for nxt in graph[ch]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return "".join(order) if len(order) == len(graph) else ""
