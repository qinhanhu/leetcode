class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        dp = []
        for _ in range(len(prices)):
            dp.append([0] * (2 * k))
        for j in range(len(dp[0])):
            # hold
            if j % 2 == 0:
                dp[0][j] = -prices[0]
        
        for i in range(1, len(prices)):
            for j in range(len(dp[i])):
                # hold
                # 第一次买入 特殊
                if j == 0:
                    dp[i][j] = max(dp[i-1][j], -prices[i])
                # 第j次买入 j>1
                elif j % 2 == 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])     
                # not hold
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i])
                

        return dp[-1][-1]