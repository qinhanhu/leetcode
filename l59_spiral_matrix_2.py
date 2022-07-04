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

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row, col = 0, 0
        deltaRow, deltaCol = 0, 1
        
        res = []
        for _ in range(n):
            res.append([-1] * n)
        i = 1
        while i <= n * n:
            res[row][col] = i
            
            if row + deltaRow < 0 or row + deltaRow > n - 1 or col + deltaCol < 0 or col + deltaCol > n - 1 or res[row + deltaRow][col + deltaCol] != -1:
                deltaRow, deltaCol = deltaCol, -deltaRow
            
            row += deltaRow
            col += deltaCol
            i += 1
        
        return res