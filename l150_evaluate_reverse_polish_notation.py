class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        for s in tokens:
            if s not in op:
                stack.append(int(s))
            else:
                right = stack.pop()
                left = stack.pop()
                if s == '+':
                    stack.append(left + right)
                elif s == '-':
                    stack.append(left - right)
                elif s == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
        return stack[0]
