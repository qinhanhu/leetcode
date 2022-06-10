class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # ubounded knapsack problem
        # dp[j] = if s can be segmented(true or false). len(s) = j
        # dp[j] = dp[j-len(wordDict[i])] and s[j-len(wordDict[i]):j] == wordDict[i] 

        dp = [False] * (len(s)+1)
        dp[0] = True
        # 遍历背包
        for j in range(len(s)+1):
            # 遍历物品
            for word in wordDict:
                if j >= len(word):
                    dp[j] = dp[j] or (dp[j-len(word)] and word == s[j-len(word):j])
            # print(dp)
        return dp[-1]