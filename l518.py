class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]
            # print(dp)

        # for j in range(amount+1):
        #     for i in range(len(coins)):
        #         if j >= coins[i]: 
        #             dp[j] += dp[j-coins[i]]
        #     print(dp)
        return dp[-1]