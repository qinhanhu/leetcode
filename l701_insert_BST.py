# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root:
            return node
        cur = root
        pre = None
        while cur:
            pre = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
                
        if pre.val > val:
            pre.left = node
        else:
            pre.right = node
        return root
        