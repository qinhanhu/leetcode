class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10 ** 9 + 7
        if maxMove == 0:
            return 0
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n):
                dp[i].append([])
                for k in range(maxMove+1):
                    dp[i][j].append(0)

        # init
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j][1] += 1
                if i == m - 1:
                    dp[i][j][1] += 1
                if j == 0:
                    dp[i][j][1] += 1
                if j == n - 1:
                    dp[i][j][1] += 1
        # print(dp)
        for k in range(2, maxMove+1):
            for i in range(m):
                for j in range(n):
                    # dp[i][j][k] = dp[i][j][k-1]
                    if j != 0:
                        dp[i][j][k] += dp[i][j-1][k-1] % mod
                    if i != 0:
                        dp[i][j][k] += dp[i-1][j][k-1] % mod
                    if j != n-1:
                        dp[i][j][k] += dp[i][j+1][k-1] % mod
                    if i != m-1:
                        dp[i][j][k] += dp[i+1][j][k-1] % mod
        # print(dp)
        return sum(dp[startRow][startColumn]) % mod