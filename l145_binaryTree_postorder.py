# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postOrder(node: TreeNode, res: List) -> None:
            if node is None:
                return
            postOrder(node.left, res)
            postOrder(node.right, res)
            res.append(node.val)
        
        res = []
        postOrder(root, res)
        return res  


# 迭代1
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        if root:
            stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]


# 统一迭代法
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        if root:
            stack.append(root)
        while stack:
            cur = stack[-1]
            if cur:
                stack.pop()
                # 左右中
                stack.append(cur)   # 中
                stack.append(None)

                if cur.right:   # 右
                    stack.append(cur.right)

                if cur.left:    # 左
                    stack.append(cur.left)
            else:
                stack.pop() # pop None node
                cur = stack.pop()
                res.append(cur.val)
        return res