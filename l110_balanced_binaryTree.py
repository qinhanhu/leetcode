# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(node: TreeNode) -> int:
            if not node:
                return 0
            leftHight = getHeight(node.left)
            rightHight = getHeight(node.right)
            if leftHight == -1 or rightHight == -1:
                return -1
            elif leftHight == rightHight:
                return leftHight + 1
            elif abs(leftHight - rightHight) > 1:
                return -1
            else:
                return max(leftHight, rightHight) + 1
        return getHeight(root) != -1
            