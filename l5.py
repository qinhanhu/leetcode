class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(s, left, right):
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left, right
        
        res = 0
        L, R = 0, 0
        for i in range(len(s)):
            l1, r1 = expandAroundCenter(s, i, i)
            l2, r2 = expandAroundCenter(s, i, i+1)
            # print(l1,r1)
            # print(l2,r2)
            if r1 - l1 - 1 > res:
                L = l1+1
                R = r1-1
                res = r1 - l1 - 1
            if r2 - l2 - 1 > res:
                L = l2+1
                R = r2-1
                res = r2 - l2 - 1
        return s[L:R+1]
