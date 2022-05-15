# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        while root:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                break
        
        cur = root
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right
            cur = cur.left
        cur = root
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right
        return root

                    
