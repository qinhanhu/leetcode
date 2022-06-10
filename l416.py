class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        find if one subset's sum is sum(nums) / 2
        0-1 knapsack: N items, item i weighting nums[i] pounds and also worth nums[i] dollars. The knapsack can take sum(nums) / 2 pounds.
        W = sum(nums) / 2
        wi = nums[i]
        vi = nums[i]
        If the knapsack is exactly full of items that the capacity is W, return True.
        dp[j] is the max of value we carried when the capacity is j.
        """
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = int(total / 2)
        # 1 dimension dp array: 
        dp = [0] * (target + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(len(dp)-1, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        # print(dp)
        return dp[-1] == target


        # 2 dimension dp array:
        # dp[i][j] = when knapsack's capacity is j, the max value we carried from items indexed within 0 to i.
        # dp = []
        # for i in range(n):
        #     dp.append([0] * (target + 1))
        
        # for i in range(n):
        #     for j in range(0, target + 1):
        #         if j < nums[i]:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i-1][j - nums[i]] + nums[i])
        # #print(dp)
        # return dp[-1][-1] == target




