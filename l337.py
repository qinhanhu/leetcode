# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def postorder(root) -> List[int]:
            # dp[0] is the maximum amount of money when u broke cur node(house),
            # dp[1] is ~ when u dont broke cur node
            if not root:
                return [0, 0]
            
            leftDP = postorder(root.left)
            rightDP = postorder(root.right)

            # broke cur node
            curDP = [0, 0]
            curDP[0] = root.val + leftDP[1] + rightDP[1]
            # dont broke cur node
            curDP[1] = max(leftDP[0], leftDP[1]) + max(rightDP[0], rightDP[1])
            return curDP
        
        dp = postorder(root)
        return max(dp[0], dp[1])
        
            
            