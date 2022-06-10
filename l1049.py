class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        """
        dp[j] = when capacity is j, the max value we carried

        we could try to divide stones into 2 stacks of equal weight
        """
        
        total = sum(stones)
        target = total // 2
        dp = [0] * (target+1)
        dp[0] = 0
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return total - dp[target] - dp[target]