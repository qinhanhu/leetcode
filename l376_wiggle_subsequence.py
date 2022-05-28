class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        predif = curdif = 0
        res = 1
        for i in range(0, len(nums) - 1):
            curdif = nums[i+1] - nums[i]
            if (predif <= 0 and curdif > 0) or (predif >= 0 and curdif < 0): 
                res += 1
                predif = curdif
        return res
