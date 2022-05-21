# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root: TreeNode) -> None:
            if not root:
                return
            inorder(root.right)
            self.cnt += root.val
            root.val = self.cnt
            inorder(root.left)
        
        inorder(root)
        return root
        