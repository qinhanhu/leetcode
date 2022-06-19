class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # dp[i] is the the length of the longest subsequence that ends with nums[i]
        if len(nums) < 2:
            return len(nums)
        dp = [1] * len(nums)
        _max = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] =  dp[i-1] + 1
            _max = max(_max, dp[i])
        return _max