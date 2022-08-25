class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0] * (m+n)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                val = int(num2[i]) * int(num1[j])
                _sum = res[i+j+1] + val
                res[i+j+1] = _sum % 10
                res[i+j] += int(_sum / 10)
        for start in range(len(res)):
            if res[start] != 0:
                break
        return "".join(list(map(str, res[start:])))