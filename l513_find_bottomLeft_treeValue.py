# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = deque()
        res = 0
        if root:
            que.append(root)
            res = root.val
        while len(que) > 0:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if i == 0:
                    res = cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return res