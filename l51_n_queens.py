class Solution:
    def __init__(self):
        self.res = []
        self.rows = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(n: int, row: int):
            if len(self.rows) == n:
                self.res.append(self.rows[:])
                return

            for i in range(n):
                if not isValid(row, i):
                    continue
                curRow = "." * i + "Q" + "." * (n-i-1)
                self.rows.append(curRow)
                backtracking(n, row+1)
                self.rows.pop()

        def isValid(row: int, col: int) -> bool:
            if row < 1:
                return True
            # same col
            for r in range(0, row):
                if self.rows[r][col] == 'Q':
                    return False
            # 45 degree
            for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if self.rows[r][c] == 'Q':
                    return False
            # 135 degree
            for r, c in zip(range(row-1, -1, -1), range(col+1, n)):
                if self.rows[r][c] == 'Q':
                    return False

            return True

        backtracking(n, 0)
        return self.res

                    
