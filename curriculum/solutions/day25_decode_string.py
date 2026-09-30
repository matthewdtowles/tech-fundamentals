class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # (text_before_bracket, repeat_count)
        current, count = "", 0
        for ch in s:
            if ch.isdigit():
                count = count * 10 + int(ch)
            elif ch == "[":
                stack.append((current, count))
                current, count = "", 0
            elif ch == "]":
                before, k = stack.pop()
                current = before + current * k
            else:
                current += ch
        return current
