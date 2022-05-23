class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, startIndex):
            self.res.append(self.path[:])
            if startIndex == len(nums):
                return
            
            for i in range(startIndex, len(nums)):
                self.path.append(nums[i])
                backtracking(nums, i+1)
                self.path.pop()
        
        backtracking(nums, 0)
        return self.res


