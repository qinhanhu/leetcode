# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        que = deque()
        if root:
            que.append(root)
        res = []
        while len(que) > 0:
            levelNodes = []
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                levelNodes.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(levelNodes)
        return res