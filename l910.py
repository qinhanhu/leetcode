class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            _max = max(nums[-1] - k, nums[i] + k)
            _min = min(nums[0] + k, nums[i+1] - k)
            res = min(res, _max - _min)
        return res
