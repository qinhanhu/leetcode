class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.pathSum = 0
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(candidates, target, startIndex):
            if self.pathSum == target:
                self.res.append(self.path[:])
                return
            
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i-1]:
                    continue
                if self.pathSum + candidates[i] > target:
                    return
                self.path.append(candidates[i])
                self.pathSum += candidates[i]
                backtracking(candidates, target, i+1)
                self.path.pop()
                self.pathSum -= candidates[i]
            
        candidates.sort()
        backtracking(candidates, target, 0)
        return self.res
        