class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for i, v in enumerate(nums):
            if v in diffMap:
                return [i, diffMap[v]] 
            diff = target - v
            diffMap[diff] = i
        return None