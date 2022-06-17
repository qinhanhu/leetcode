class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                res += profit
        return res


# DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0]: the max profit you can get when u hold one stock within 0-ith days.
        dp[i][1]: the max profit ~ when u dont hold any stock ~.
        """

        dp = []
        for _ in range(len(prices)):
            dp.append([0, 0])
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return max(dp[-1][0], dp[-1][1])