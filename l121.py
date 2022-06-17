class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i] is the max profit we can get between 0-ith days
        dp[i] = max(dp[i-1], prices[i] - min(price[:i+1]))
        """

        _min = prices[0]
        dp = [0] * len(prices)
        dp[0] = 0
        for i in range(1, len(prices)):
            if _min > prices[i]:
                _min = prices[i]
            dp[i] = max(dp[i-1], prices[i] - _min)
        # print(dp)
        return dp[-1]