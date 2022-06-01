class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        maxRange = nums[0]
        i = 0
        while i <= maxRange:
            if maxRange >= len(nums) - 1:
                return True
            maxRange = max(maxRange, nums[i] + i)
            i += 1
        return False