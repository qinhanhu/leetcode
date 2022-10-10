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

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))