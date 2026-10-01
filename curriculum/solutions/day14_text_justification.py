from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines, i = [], 0
        while i < len(words):
            j, width = i, 0  # words[i:j] fit on this line; width = letters only
            while j < len(words) and width + len(words[j]) + (j - i) <= maxWidth:
                width += len(words[j])
                j += 1
            line_words, gaps = words[i:j], j - i - 1
            if j == len(words) or gaps == 0:
                line = " ".join(line_words).ljust(maxWidth)
            else:
                base, extra = divmod(maxWidth - width, gaps)
                line = "".join(w + " " * (base + (k < extra)) for k, w in enumerate(line_words[:-1])) + line_words[-1]
            lines.append(line)
            i = j
        return lines
