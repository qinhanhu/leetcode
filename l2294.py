class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        _min = nums[0]
        res = 1
        for i in range(n):
            if nums[i] - _min > k:
                _min = nums[i]
                res += 1
        return res