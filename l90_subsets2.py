class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        def backtracking(nums:List[int], startIndex:int):
            self.result.append(self.path[:])
            if startIndex == len(nums):
                return
            
            for i in range(startIndex, len(nums)):
                if i != startIndex and nums[i] == nums[i-1]:
                    continue
                self.path.append(nums[i])
                backtracking(nums, i+1)
                self.path.pop()
            
        nums.sort()
        backtracking(nums, 0)
        return self.result

        