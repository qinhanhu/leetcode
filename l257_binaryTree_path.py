# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def backtrack(node: TreeNode, path: List, res: List):
            if not node.left and not node.right:
                path.append(str(node.val))
                res.append("->".join(path))
                return
            
            path.append(str(node.val))
            if node.left:
                backtrack(node.left, path, res)
                path.pop()
            if node.right:
                backtrack(node.right, path, res)
                path.pop()
        
        if not root:
            return []
        res = []
        path = []
        backtrack(root, path, res)
        return res