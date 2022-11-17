# https://labuladong.github.io/algo/2/21/38/

# https://leetcode.cn/problems/maximum-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        root = TreeNode()
        _max = -1
        idx = 0
        for i in range(len(nums)):
            if _max < nums[i]:
                _max = nums[i]
                idx = i
        root.val = _max
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root

# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val2idx = dict()
        for i, val in enumerate(inorder):
            val2idx[val] = i

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, val2idx)
    
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd, val2idx):
        if preStart > preEnd:
            return None
        
        val = preorder[preStart]
        idx = val2idx[val]
        leftSize = idx - inStart
        rightSize = inEnd - idx

        root = TreeNode(val=val)
        root.left = self.build(preorder, preStart+1, preStart+leftSize, inorder, inStart, idx-1, val2idx)
        root.right = self.build(preorder, preStart+leftSize+1, preEnd, inorder, idx+1, inEnd, val2idx)
        return root

# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val2idx = dict()
        for i, val in enumerate(inorder):
            val2idx[val] = i

        return self.build(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1, val2idx)
    
    def build(self, postorder, postStart, postEnd, inorder, inStart, inEnd, val2idx):
        if postStart > postEnd:
            return None
        
        val = postorder[postEnd]
        idx = val2idx[val]
        leftSize = idx - inStart
        rightSize = inEnd - idx

        root = TreeNode(val=val)
        root.left = self.build(postorder, postStart, postStart+leftSize-1, inorder, inStart, idx-1, val2idx)
        root.right = self.build(postorder, postEnd-rightSize, postEnd-1, inorder, idx+1, inEnd, val2idx)
        return root

# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:          
        val2idx = dict()
        for i, val in enumerate(postorder):
            val2idx[val] = i

        return self.build(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1, val2idx)
    
    def build(self, preorder, preStart, preEnd, postorder, postStart, postEnd, val2idx):
        if preStart > preEnd:
            return None
        if preStart == preEnd:
            return TreeNode(val=preorder[preStart])
            
        rootVal = preorder[preStart]
        leftVal = preorder[preStart+1]

        idx = val2idx[leftVal]
        leftSize = idx - postStart + 1
        rightSize = postEnd - idx - 1

        root = TreeNode(val=rootVal)
        root.left = self.build(preorder, preStart+1, preStart+leftSize, postorder, postStart, idx, val2idx)
        root.right = self.build(preorder, preStart+leftSize+1, preEnd, postorder, idx+1, postEnd-1, val2idx)
        return root

# 序列化反序列化 - 前序遍历
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/submissions/
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
        result = []
        self.serializeHelper(root, result)
        return ",".join(result)
    
    def serializeHelper(self, root, result):
        if not root:
            result.append("#")
            return
        
        result.append(str(root.val))
        self.serializeHelper(root.left, result)
        self.serializeHelper(root.right, result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        que = collections.deque(data.split(","))
        root = self.deserializeHelper(que)
        return root
    
    def deserializeHelper(self, que):
        if not que:
            return None
        cur = que.popleft()
        if cur == "#":
            return None
        root = TreeNode(int(cur))
        root.left = self.deserializeHelper(que)
        root.right = self.deserializeHelper(que)
        return root

# L428 N叉树
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
