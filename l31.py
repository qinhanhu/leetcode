class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = n - 2
        j = n - 1
        # 1. find nums[i] < nums[j]
        while i >= 0:
            if nums[i] < nums[j]:
                break
            i -= 1
            j -= 1
        if i >= 0: # if i == -1, j==0. means nums = [3,2,1]
            # 2. in nums[j:], find the nums[x] > nums[i], j <= x <= n - 1
            x = n - 1
            while x >= j:
                if nums[x] > nums[i]:
                    break
                x -= 1
            # swap
            nums[x], nums[i] = nums[i], nums[x]

        # 3. reverse nums[j:]
        left = j
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        
        