class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        res = 0
        i = 0
        preMax = 0
        worker.sort()
        for work in worker:
            while i < len(jobs) and work >= jobs[i][0]:
                if jobs[i][1] >= preMax:
                    preMax = jobs[i][1]
                i += 1

            res += preMax
        return res
            
