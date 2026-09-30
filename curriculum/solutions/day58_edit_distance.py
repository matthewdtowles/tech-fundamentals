class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = list(range(len(word2) + 1))  # distance from word1[:0] to each prefix of word2
        for i, a in enumerate(word1, 1):
            row = [i]
            for j, b in enumerate(word2, 1):
                if a == b:
                    row.append(prev[j - 1])
                else:
                    row.append(1 + min(prev[j], row[j - 1], prev[j - 1]))  # delete, insert, replace
            prev = row
        return prev[-1]
