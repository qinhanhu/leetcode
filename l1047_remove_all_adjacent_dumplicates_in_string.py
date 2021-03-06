class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)