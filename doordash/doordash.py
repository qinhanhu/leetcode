# L45: https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy: For i-th jumb, we iterate from index(i) to index(i+nums[i]), which is the farthest index(maxRange) we can reach for now. Meanwhile, update the farthest index we can reach untill maxRange == n - 1.
        
        n = len(nums)
        if n < 2:
            return 0
        
        maxRange = nums[0]
        cur = 0
        step = 1
        
        while maxRange < n - 1:
            for i in range(cur, maxRange + 1):
                maxRange = max(maxRange, i + nums[i])
                cur += 1
            step += 1
        return step