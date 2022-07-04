class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        delr, delc = 0, 1
        res = []
        while len(res) < m * n:
            res.append(matrix[r][c])
            matrix[r][c] = -101
            
            if r + delr < 0 or r + delr > m - 1 or c + delc < 0 or c + delc > n - 1 or matrix[r + delr][c + delc] == -101:
                delr, delc = delc, -delr
            
            r += delr
            c += delc
        
        return res
        