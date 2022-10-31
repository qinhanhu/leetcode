# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.postorder(root)
        return self.max

    def postorder(self, root) -> int:
        if not root:
            return 0
        
        leftDepth = self.postorder(root.left)
        rightDepth = self.postorder(root.right)
        
        self.max = max(self.max, leftDepth + rightDepth)
        return max(leftDepth, rightDepth) + 1