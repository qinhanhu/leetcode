class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(n, k, startIndex):
            if len(self.path) == k:
                self.res.append(self.path[:])
                return
            
            # 剪枝
            demandNums = k - len(self.path)
            for i in range(startIndex, (n-demandNums+1)+1):
                self.path.append(i)
                backtracking(n, k, i+1)
                self.path.pop()
        
        backtracking(n, k, 1)
        return self.res
            
