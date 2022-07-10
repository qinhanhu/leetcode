class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGre = {}
        for i in range(len(nums2)):
            nextGre[nums2[i]] = -1
        stack = [0]
        for i in range(1, len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                nextGre[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)
        res = []
        for i in range(len(nums1)):
            res.append(nextGre[nums1[i]])
        return res