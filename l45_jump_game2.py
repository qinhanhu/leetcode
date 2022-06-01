class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        maxRange = nums[0]
        index = 0
        cnt = 1
        while maxRange < len(nums) - 1:
            for i in range(index, maxRange+1):
                if nums[i] + i > maxRange:
                    maxRange = nums[i] + i
                    index = i
            cnt += 1
        return cnt
        