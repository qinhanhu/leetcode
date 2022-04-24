class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                t = target - (nums[i] + nums[j])
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[left] + nums[right]
                    if total > t:
                        right -= 1
                    elif total < t:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left< right and nums[left] == nums[left+1]:
                            left += 1
                        while left< right and nums[right] == nums[right-1]:
                            right -= 1   
                        left += 1
                        right -= 1
        return res              