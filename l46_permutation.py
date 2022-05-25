class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums):
            if len(self.path) == len(nums):
                self.res.append(self.path[:])
                return

            for i in range(len(nums)):
                if nums[i] in self.path:
                    continue
                self.path.append(nums[i])
                backtracking(nums)
                self.path.pop()
        
        backtracking(nums)
        return self.res
        