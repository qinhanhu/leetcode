# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrder(node: TreeNode, res: List) -> None:
            if node is None:
                return
            inOrder(node.left, res)
            res.append(node.val)
            inOrder(node.right, res)
        
        res = []
        inOrder(root, res)
        return res  



# 迭代1
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res


# 统一迭代法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        if root:
            stack.append(root)
        while stack:
            cur = stack[-1]
            if cur:
                stack.pop()
                # 左中右
                if cur.right:   # 右
                    stack.append(cur.right)

                stack.append(cur)   # 中
                stack.append(None) 

                if cur.left:    # 左
                    stack.append(cur.left)
            else:
                stack.pop() # pop None node
                cur = stack.pop()
                res.append(cur.val)
        return res