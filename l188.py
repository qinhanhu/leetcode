class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = []
        for _ in range(len(prices)):
            dp.append([0] * (2 * k + 1))
        for j in range(len(dp[0])):
            # hold
            if j % 2 == 1:
                dp[0][j] = -prices[0]
        
        for i in range(1, len(prices)):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j]
                # hold
                elif j % 2 == 1:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
                # not hold
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i])
                

        return dp[-1][-1]
                