# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        que = deque()
        if root:
            que.append(root)
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root