class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] is the maximum length of the common subarray of A which ends with i-th item of nums1 and B ends with j-th item of nums2, i,j >= 1

        dp = []
        for _ in range(len(nums1)+1):
            dp.append([0] * (len(nums2)+1))
        
        _max = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                _max = max(_max, dp[i][j])
                
        return _max
            


        

