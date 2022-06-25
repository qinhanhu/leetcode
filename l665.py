class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True
        neg = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] < 0:
                neg += 1
                if neg > 1:
                    return False
                if i < n-1 and nums[i+1] < nums[i-1]:
                    if i - 1 >= 1 and nums[i-2] > nums[i]:
                            return False
        return True
                        
            
        