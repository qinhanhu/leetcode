# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
            res.append(sum(levelNodes) / size)
        return res