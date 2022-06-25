class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        dp[i][j] is the minimum cost of 0-ith houses if nums[i] house's cost is costs[i][j]
        """

        n = len(costs)
        dp = []
        for _ in range(n):
            dp.append([0] * 3)
        
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        
        return min(dp[-1][0], dp[-1][1], dp[-1][2])

        