class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        prev = [0] * (len(text2) + 1)  # row for text1[:i - 1]
        for a in text1:
            row = [0]
            for j, b in enumerate(text2):
                row.append(prev[j] + 1 if a == b else max(prev[j + 1], row[j]))
            prev = row
        return prev[-1]
