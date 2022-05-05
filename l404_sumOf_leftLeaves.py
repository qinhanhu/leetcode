# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftSubSum = self.sumOfLeftLeaves(root.left)
        rightSubSum = self.sumOfLeftLeaves(root.right)

        midSum = 0
        if root.left and not root.left.left and not root.left.right:
            midSum = root.left.val

        return midSum + leftSubSum + rightSubSum