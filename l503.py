class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nextG = [-1] * len(nums)
        stack = [0]
        for i in range(1, len(nums) * 2):
            while stack and nums[i % len(nums)] > nums[stack[-1] % len(nums)]:
                nextG[stack[-1] % len(nums)] = nums[i % len(nums)]
                stack.pop()
            stack.append(i)
        return nextG