class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j] is the max lenth of the side of the square such that matrix[i][j] is the right-bottom most element of it and it contain only 1's.
        """

        dp = []
        m = len(matrix)
        n = len(matrix[0])
        for _ in range(m):
            dp.append([0] * n)
        maxSide = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            maxSide = max(maxSide, dp[i][0])

        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            maxSide = max(maxSide, dp[0][j])
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        # print(dp)
        return maxSide * maxSide

