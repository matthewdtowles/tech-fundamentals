class Solution:
    def isValid(self, s: str) -> bool:
        opener = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in opener:
                if not stack or stack.pop() != opener[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
