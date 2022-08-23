# l54. Spiral Matrix 1
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
        
# l59. Spiral Matrix 2
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

# l885. Spiral Matrix 3
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        r, c = rStart, cStart
        deltar, deltac = 0, 1
        rotateCnt = 0
        step = 1
        
        while len(res) < rows * cols:
            if 0 <= r <= rows - 1 and 0 <= c <= cols - 1:
                res.append((r, c))
            
            if r + deltar > rStart + step or r + deltar < rStart - step or c + deltac > cStart + step or c + deltac < cStart - step:
                if rotateCnt == 4:
                    step += 1
                    rotateCnt = 0
                else:
                    deltar, deltac = deltac, -deltar
                    rotateCnt += 1
            
            r += deltar
            c += deltac
        return res
                    
            
# l2326 Spiral Matrix 4
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        row, col = 0, 0
        deltaRow, deltaCol = 0, 1
        
        res = []
        for _ in range(m):
            res.append([-1] * n)
        
        while head:
            res[row][col] = head.val
            
            if row + deltaRow < 0 or row + deltaRow > m - 1 or col + deltaCol < 0 or col + deltaCol > n - 1 or res[row + deltaRow][col + deltaCol] != -1:
                deltaRow, deltaCol = deltaCol, -deltaRow
            
            row += deltaRow
            col += deltaCol
            head = head.next
        
        return res
            
            