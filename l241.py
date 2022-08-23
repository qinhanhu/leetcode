class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(len(expression)):
            ch = expression[i]
            if ch in ["+", "-", "*"]:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for x in left:
                    for y in right:
                        if ch == "+":
                            res.append(x + y)
                        elif ch == "-":
                            res.append(x - y)
                        elif ch == "*":
                            res.append(x * y)
        if not res:
            res.append(int(expression))
        return res

