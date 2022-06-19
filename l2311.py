class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        if int(s, 2) <= k:
             return len(s)
        if int(s[-1]) > k:
            return 0
        
        dp = [0] * len(s)
        dp[len(s) - 1] = 1
        for i in range(len(s)-2, -1, -1):
            if int(s[i:],2) <= k:
                dp[i] = dp[i+1] + 1
            elif s[i] == '0':
                dp[i] = dp[i+1] + 1
            else:
                dp[i] = dp[i+1]
        # print(dp)
        return dp[0]
            
        