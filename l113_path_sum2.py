# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def pathSumRecurse(node: TreeNode, curSum: int, targetSum: int, curPath:List, res: List):
            if not node.left and not node.right:
                if curSum == targetSum:
                    res.append(curPath[:])
                return
            
            if node.left:
                curSum += node.left.val
                curPath.append(node.left.val)
                pathSumRecurse(node.left, curSum, targetSum, curPath, res)
                curSum -= node.left.val
                curPath.pop()

            if node.right:
                curSum += node.right.val
                curPath.append(node.right.val)
                pathSumRecurse(node.right, curSum, targetSum, curPath, res)
                curSum -= node.right.val
                curPath.pop()

        if not root:
            return []
        res = []
        curPath = [root.val]
        curSum = root.val
        pathSumRecurse(root, curSum, targetSum, curPath, res)
        return res