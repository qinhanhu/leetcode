class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # dp[i] is the length of the longest subsequence which ends with nums[i]
        dp = [1] * len(nums)
        _max = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            _max = max(_max, dp[i])
        return _max