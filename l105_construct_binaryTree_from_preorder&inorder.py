# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break
        leftInorder = inorder[:i]
        rightInorder = inorder[i+1:]

        preorder = preorder[1:]
        leftPreorder = preorder[:len(leftInorder)]
        rightPreorder = preorder[len(leftInorder):]

        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        return root