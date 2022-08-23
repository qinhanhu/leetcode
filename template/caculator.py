from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        
        def helper(s:list):
            stack = []
            sign = "+"
            num = 0

            while len(s) > 0:
                c = s.popleft()
                if c.isdigit():
                    num = 10 * num + int(c)
                if c == "(":
                    num = helper(s)
                if (not c.isdigit() and c != " ") or len(s) == 0:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack[-1] = stack[-1] * num
                    elif sign == "/":
                        stack[-1] = int(stack[-1] / float(num))
                    sign = c
                    num = 0
                if c == ")":
                    break
            return sum(stack)
        
        return helper(deque(s))
                        


        