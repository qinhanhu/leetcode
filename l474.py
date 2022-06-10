class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        
        # 遍历物品
        for i in range(len(strs)):
            zeroCnt = strs[i].count('0')
            oneCnt = strs[i].count('1')
            
            # 遍历背包容量-倒序
            for x in range(m, zeroCnt-1, -1):
                for y in range(n, oneCnt-1, -1):
                    dp[x][y] = max(dp[x][y], dp[x-zeroCnt][y-oneCnt] + 1)
        return dp[-1][-1]