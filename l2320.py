class Solution:
    def countHousePlacements(self, n: int) -> int:
        m = 1e9 + 7
        dp = []
        for _ in range(n):
            dp.append([0] * 2)
        
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
        # print(dp)
        res = dp[-1][0] + dp[-1][1]
        return int(self.mod(str(res * res), m))
    
    def mod(self, num, a):
 
        # Initialize result
        res = 0

        # One by one process all digits
        # of 'num'
        for i in range(0, len(num)):
            res = (res * 10 + int(num[i])) % a

        return res
        
        