from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        longest = max(map(len, words))
        ok = [True] + [False] * len(s)  # ok[i]: s[:i] can be segmented
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - longest), i):
                if ok[j] and s[j:i] in words:
                    ok[i] = True
                    break
        return ok[-1]
