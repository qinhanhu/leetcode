class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)
        index = len(nums) - 1
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res[index] = nums[left] * nums[left]
                left += 1
            else:
                res[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return res