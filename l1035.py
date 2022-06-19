class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] is the LCS of text1[:i] and text2[:j]
        
        dp = []
        n = len(nums1)
        m = len(nums2)
        for _ in range(n+1):
            dp.append([0] * (m+1))
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]