from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts = Counter(s1.split() + s2.split())
        return [word for word, c in counts.items() if c == 1]
