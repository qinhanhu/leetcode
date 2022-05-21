class Solution:
    def __init__(self):
        self.pathSum = 0
        self.path = []
        self.result = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtracking(k, n, startIndex):
            if self.pathSum > n:
                return
                
            if len(self.path) == k:
                if self.pathSum == n:
                    self.result.append(self.path[:])
                return 
            demandNums = k - len(self.path)
            for i in range(startIndex, (9 - demandNums + 1) + 1):
                self.path.append(i)
                self.pathSum += i
                backtracking(k, n, i + 1)
                self.path.pop()
                self.pathSum -= i
            
        backtracking(k, n, 1)
        return self.result
