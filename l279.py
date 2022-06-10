class Solution:
    def numSquares(self, n: int) -> int:
        # unbounded knapsack problem
        # dp[j] = the least number of perfect square numbers that sum to j
        # dp[j] = min(dp[j], dp[j-i*i] + 1)

        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            for j in range(i*i, n+1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
            # print(dp)
        return dp[-1]
        