# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        # 1. find root
        root = TreeNode(postorder[-1])
        if len(postorder) == 1:
            return root
        # 2. divide inorder slice
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break
        leftInorder = inorder[0:i]
        rightInorder = inorder[i+1:]
        # print(leftInorder, rightInorder)
        # 3. divide postorder slice
        postorder = postorder[:-1]
        leftPostorder = postorder[:len(leftInorder)]
        rightPostorder = postorder[len(leftInorder):]
        # print(leftPostorder, rightPostorder)
        # 4. recurse
        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)
        return root