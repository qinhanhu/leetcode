class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, used):
            if len(self.path) == len(nums):
                self.res.append(self.path[:])
                return

            for i in range(len(nums)):
                if used[i] is True:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] is False:
                    continue
                self.path.append(nums[i])
                used[i] = True
                backtracking(nums, used)
                self.path.pop()
                used[i] = False

        used = [False] * len(nums)
        nums.sort()
        backtracking(nums, used)
        return self.res
        