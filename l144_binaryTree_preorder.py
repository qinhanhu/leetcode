# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preOrder(node: TreeNode, res: List) -> None:
            if node is None:
                return
            res.append(node.val)
            preOrder(node.left, res)
            preOrder(node.right, res)
        
        res = []
        preOrder(root, res)
        return res        
            

# 迭代法1
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        if root:
            stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

# 统一迭代法
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        if root:
            stack.append(root)
        while stack:
            cur = stack[-1]
            if cur:
                stack.pop()
                # 中左右
                if cur.right:   # 右
                    stack.append(cur.right)

                if cur.left:    # 左
                    stack.append(cur.left)

                stack.append(cur)   # 中
                stack.append(None)
            else:
                stack.pop() # pop None node
                cur = stack.pop()
                res.append(cur.val)
        return res













