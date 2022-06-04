class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        cash = [0, 1]
        for i in range(2, n+1):
            cash.append(cash[i-1] + cash[i-2])
        return cash[-1]