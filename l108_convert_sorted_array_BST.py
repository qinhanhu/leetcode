# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(nums, left, right):
            if left > right:
                return
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = buildBST(nums, left, mid-1)
            root.right = buildBST(nums, mid+1, right)
            return root

        return buildBST(nums, 0, len(nums)-1)