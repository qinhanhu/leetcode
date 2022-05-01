# 递归法 前中后序
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






# 迭代法 前中后序
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


# 层序遍历 level order traversal
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