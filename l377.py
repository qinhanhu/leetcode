class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        # 求排列外层遍历容量，内层物品。
        # 求组合外层遍历物品，内层容量（0-1逆序，完全正序）。
        for j in range(target+1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j-nums[i]]
        return dp[-1]