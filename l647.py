class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def detect(s, l, r) -> int:
            res = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            return  res


        res = 0
        for i in range(len(s)):
            res += detect(s, i, i) + detect(s, i, i+1)

        return res
        
        