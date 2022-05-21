class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.pathSum = 0
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(candidates, target, startIndex):
            if self.pathSum > target:
                return
            if self.pathSum == target:
                self.res.append(self.path[:])
                return
            
            for i in range(startIndex, len(candidates)):
                # if self.pathSum + candidates[i] > target:
                #     return
                self.path.append(candidates[i])
                self.pathSum += candidates[i]
                backtracking(candidates, target, i)
                self.path.pop()
                self.pathSum -= candidates[i]
            
        
        backtracking(candidates, target, 0)
        return self.res
        