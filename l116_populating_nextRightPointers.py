"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        que = deque()
        if root:
            que.append(root)
        while len(que) > 0:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if i < size - 1:
                    cur.next = que[0]
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root                    
                