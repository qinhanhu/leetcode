# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        
        if p.val == q.val:
            leftSubIsSame = self.isSameTree(p.left, q.left)
            rightSubIsSame = self.isSameTree(p.right, q.right)
            if leftSubIsSame and rightSubIsSame:
                return True
        return False