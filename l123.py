class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0]: no operation
        dp[i][1]: the max profit when we hold a stock in the first transaction within i days
        dp[i][2]: ~ when we dont hold a stock in the first ~
        dp[i][3]: ~ when we hold a stock in the second trans ~
        dp[i][4]: ~ when we dont hold a stock in the second trans ~
        """
        dp = []
        for _ in range(len(prices)):
            dp.append([0] * 5)

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0
        
        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

        return dp[-1][4]

