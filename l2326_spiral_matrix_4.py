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
            
            