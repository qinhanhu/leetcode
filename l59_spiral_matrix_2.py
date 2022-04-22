class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        for _ in range(n):
            res.append([0] * n)

        loop = n // 2
        mid = n // 2
        starti, startj = 0, 0
        offset = 1
        value = 1

        while loop > 0:
            i, j = starti, startj
            cnt = n - offset
            for _ in range(cnt):
                res[i][j] = value
                value += 1
                j += 1
            for _ in range(cnt):
                res[i][j] = value
                value += 1
                i += 1
            for _ in range(cnt):
                res[i][j] = value
                value += 1
                j -= 1
            for _ in range(cnt):
                res[i][j] = value
                value += 1
                i -= 1
            loop -= 1
            starti += 1
            startj += 1
            offset += 2
        
        if n % 2 == 1:
            res[mid][mid] = value
        return res