class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        preSum = 0
        res = -1
        for i in range(len(nums)):
            rightSum = total - preSum - nums[i]
            if preSum == rightSum:
                return i
            preSum += nums[i]
        return res