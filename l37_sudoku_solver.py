class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtracking(board) -> bool:
            rowsLen = colsLen = 9
            for i in range(rowsLen):
                for j in range(colsLen):
                    if board[i][j] != '.':
                        continue
                    for val in range(1, 10):
                        if not isValid(i, j, str(val), board):
                            continue
                        board[i][j] = str(val)
                        if backtracking(board) is True:
                            return True
                        board[i][j] = '.'
                    return False
            return True
                        
        def isValid(row, col, val, board) -> bool:
            rowsLen = colsLen = 9
            # same row
            for j in range(colsLen):
                if board[row][j] == val:
                    return False
            # same col
            for i in range(rowsLen):
                if board[i][col] == val:
                    return False
            # 3 * 3
            startRow = int(row / 3) * 3
            startCol = int(col / 3) * 3
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == val:
                        return False
            return True

        backtracking(board)
        return


            