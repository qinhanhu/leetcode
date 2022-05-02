# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = rightDepth = 0
        cur = root
        while cur.left:
            cur = cur.left
            leftDepth += 1
        while cur.right:
            cur = cur.right
            rightDepth += 1
        if leftDepth == rightDepth:
            return (2**leftDepth - 1) + 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1