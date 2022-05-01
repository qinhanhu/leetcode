"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                if node.children:
                    for child in node.children:
                        que.append(child)
            res.append(levelNodes)
        return res