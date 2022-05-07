# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minDif = float('inf')
        self.pre = None

    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorderTraverse(node: TreeNode) -> None:
            if not node:
                return
            
            inorderTraverse(node.left)
            if self.pre:
                self.minDif = min(self.minDif, node.val - self.pre.val)
            self.pre = node
            inorderTraverse(node.right)
        
        inorderTraverse(root)
        return self.minDif
