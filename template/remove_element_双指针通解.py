# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def process(nums, k):
            idx = 0
            for x in nums:
                if idx < k or nums[idx-k] != x:
                    nums[idx] = x
                    idx += 1
            return idx
        return process(nums, 1)


# https://leetcode.cn/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insertIndex = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex