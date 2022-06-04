# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def minCameraCover(self, root: TreeNode) -> int:
        def postorder(root) -> int:
            if not root:
                return 2
            
            left = postorder(root.left)
            right = postorder(root.right)
            # 1-camera 2-monitored 3-not monitored
            if left == right == 2:
                return 3
            elif left == 3 or right == 3:
                self.res += 1
                return 1
            elif left == 1 or right == 1:
                return 2
            
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        # root not monitored
        if postorder(root) == 3:
            self.res += 1
        return self.res
        
            
            

