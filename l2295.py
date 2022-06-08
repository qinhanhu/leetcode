class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)
        m = len(operations)
        hmap = {}
        for i in range(n):
            hmap[nums[i]] = i
            
        for i in range(m):
            ix = hmap.get(operations[i][0])
            nums[ix] = operations[i][1]
            del(hmap[operations[i][0]])
            hmap[operations[i][1]] = ix
        return nums
        