# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSumRecurse(node: TreeNode, pathSum: int, targetSum: int) -> bool:
            if not node.left and not node.right:
                if pathSum == targetSum:
                    return True
                return False

            if node.left:
                pathSum += node.left.val
                if pathSumRecurse(node.left, pathSum, targetSum):
                    return True
                pathSum -= node.left.val
            
            if node.right:
                pathSum += node.right.val
                if pathSumRecurse(node.right, pathSum, targetSum):
                    return True
                pathSum -= node.right.val
                
            return False
        
        if not root:
            return False
        return pathSumRecurse(root, root.val, targetSum)