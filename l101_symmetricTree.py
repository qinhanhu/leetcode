# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetricRecurse(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            elif left and not right:
                return False
            elif not left and right:
                return False
            elif left and right and left.val != right.val:
                return False
            # left.val == right.val
            outsideIsSym = isSymmetricRecurse(left.left, right.right)
            insideIsSym = isSymmetricRecurse(left.right, right.left)
            return outsideIsSym and insideIsSym
        
        if not root:
            return True
        return isSymmetricRecurse(root.left, root.right)