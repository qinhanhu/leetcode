# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sumMap = {}

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def postorder(node) -> int:
            if not node:
                return 0
            
            leftSum = postorder(node.left)
            rightSum = postorder(node.right)

            curSum = leftSum + rightSum + node.val
            if curSum not in self.sumMap:
                self.sumMap[curSum] = 1
            else:
                self.sumMap[curSum] += 1
            return curSum
        
        total = postorder(root)
        temp = sorted(self.sumMap.items(), reverse=True, key=lambda x:x[1])
        res = []
        for i in range(len(temp)):
            if i > 0 and temp[i][1] != temp[i-1][1]:
                break
            res.append(temp[i][0])
        return res
                
        