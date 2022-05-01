# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        if root:
            que.append(root)
        res = []
        while len(que) > 0:
            size = len(que)
            _max = float('-inf')
            for _ in range(size):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                _max = max(_max, cur.val)
            res.append(_max)
        return res