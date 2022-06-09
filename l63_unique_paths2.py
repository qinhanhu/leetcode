class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []
        for i in range(m):
            dp.append([0] * n)
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j]
                elif i == j == 0:
                    continue
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        # print(dp)
        return dp[-1][-1]