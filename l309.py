class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = []
        for _ in range(len(prices)):
            dp.append([0] * 4)
        
        # hold
        dp[0][0] = -prices[0]
        # not hold
        dp[0][1] = 0
        # cooldown
        dp[0][2] = 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            dp[i][2] = dp[i-1][1]

        return max(dp[-1][1], dp[-1][2])
