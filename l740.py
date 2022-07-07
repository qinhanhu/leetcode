from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        _max = max(nums)
        dp = [0] * (_max + 1)
        dp[1] = counter.get(1, 0)
        for i in range(2, _max + 1):
            dp[i] = max(dp[i-1], dp[i-2] + i * counter.get(i, 0))
        return dp[_max]
        