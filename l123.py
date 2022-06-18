class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0]: the max profit when we hold a stock in the first transaction within i days
        dp[i][1]: ~ when we dont hold a stock in the first ~
        dp[i][2]: ~ when we hold a stock in the second trans ~
        dp[i][3]: ~ when we dont hold a stock in the second trans ~
        """
        dp = []
        for _ in range(len(prices)):
            dp.append([0] * 4)

        # 第一次持有
        dp[0][0] = -prices[0]
        # 第一次无持有
        dp[0][1] = 0
        # 第二次持有
        dp[0][2] = -prices[0]
        # 第二次无持有
        dp[0][3] = 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] + prices[i])

        return dp[-1][3]