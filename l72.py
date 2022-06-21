class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j] is the minimum number of operations required to convert word1[:i] to word2[:j]
        if word1[i-1] == word2[j-1], dp[i][j] = dp[i-1][j-1]
        else:
            delete: dp[i][j] = dp[i-1][j] + 1
            replece: dp[i][j] = dp[i-1][j-1] + 1
            insert: dp[i][j] = dp[i][j-1] + 1
            dp[i][j] = min(dp[i-1][j-1] + 1, dp[i][j-1] + 1, dp[i-1][j] + 1)
        """ 

        dp = []
        n = len(word1)
        m = len(word2)

        for i in range(n+1):
            dp.append([0] * (m+1))
        
        dp[0][0] = 0
        for i in range(1, n+1):
            dp[i][0] = i
        
        for j in range(1, m+1):
            dp[0][j] = j
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i][j-1] + 1, dp[i-1][j] + 1)
        # print(dp)
        return dp[-1][-1]        