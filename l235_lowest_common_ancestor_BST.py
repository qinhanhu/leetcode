# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)
        if not root:
            return None
        
        if minVal <= root.val <= maxVal:
            return root
        elif root.val < minVal:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > maxVal:
            return self.lowestCommonAncestor(root.left, p, q)