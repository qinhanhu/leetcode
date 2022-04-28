class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif len(stack) == 0 or stack[-1] != char:
                return False
            elif char == stack[-1]:
                stack.pop()
        return len(stack) == 0