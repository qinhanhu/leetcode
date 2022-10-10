# 20. L297: https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.serializeHelper(root, res)
        return ",".join(res)
    
    def serializeHelper(self, root, res:list) -> None:
        if not root:
            res.append("None")
            return
        res.append(str(root.val))
        self.serializeHelper(root.left, res)
        self.serializeHelper(root.right, res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = collections.deque(data.split(","))
        return self.deserializeHelper(data)
    
    def deserializeHelper(self, que) -> 'TreeNode':
        val = que.popleft()
        if val == "None":
            return None
        node = TreeNode(int(val))
        node.left = self.deserializeHelper(que)
        node.right = self.deserializeHelper(que)
        return node
            
# 21. L428
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    # def __init__(self):
    #     self.res = ""
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = []
        self.serializeHelper(root, res)
        return ",".join(res)
    def serializeHelper(self, root, res:list):
        if not root:
            return ""
        res.append(str(root.val))
        res.append(str(len(root.children)))
        for child in root.children:
            self.serializeHelper(child, res)
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        data = collections.deque(data.split(","))
        return self.deserializeHelper(data)
        
    def deserializeHelper(self, data):
        if len(data) < 1:
            return None
        val = data.popleft()
        node = Node(int(val), [])
        size = int(data.popleft())
        for _ in range(size):
            node.children.append(self.deserializeHelper(data))
        return node