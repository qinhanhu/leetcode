# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = set()
        self.maxMode = -float('inf')
        self.count = 0
        self.pre = None

    def findMode(self, root: TreeNode) -> List[int]:
        self.inorder(root)
        return list(self.res)

    def inorder(self, root: TreeNode) -> None:
        if not root:
            return 
        
        self.inorder(root.left)
        # print(root.val, self.count, self.maxMode)
        if not self.pre:
            self.count = 1
        elif self.pre.val == root.val:
            self.count += 1
        else:
            self.count = 1

        if self.count > self.maxMode:
            self.res = set()
            self.res.add(root.val)
            self.maxMode = self.count
        elif self.count == self.maxMode:
            self.res.add(root.val)
        self.pre = root

        self.inorder(root.right)
