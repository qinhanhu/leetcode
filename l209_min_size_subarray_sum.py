class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        minLen = len(nums) + 1
        sumPre = [0] * len(nums)
        sumPre[0] = nums[0]
        for i in range(1, len(nums)):
            sumPre[i] += sumPre[i-1] + nums[i]
        while left <= right and right < len(nums):
            windowSum = sumPre[right] - sumPre[left] + nums[left]
            if windowSum >= target:
                minLen = min(minLen, right - left + 1)
                left += 1
            else:
                right += 1
        return 0 if minLen == len(nums) + 1 else minLen