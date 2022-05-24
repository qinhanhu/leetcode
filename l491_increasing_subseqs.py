class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:  
        if not nums:
            return []
        
        def backtracking(nums, startIndex):
            if len(self.path) >= 2:
                self.result.append(self.path[:])
            
            if startIndex >= len(nums):
                return

            sameLevelUsedNodes = set()
            for i in range(startIndex, len(nums)):
                if nums[i] in sameLevelUsedNodes:
                    continue
                if self.path and nums[i] < self.path[-1]:
                    continue
                sameLevelUsedNodes.add(nums[i])
                self.path.append(nums[i])
                # print(self.path, startIndex, i)
                backtracking(nums, i+1)
                self.path.pop()
        
        backtracking(nums, 0)
        return self.result
                

