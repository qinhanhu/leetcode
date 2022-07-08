class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = [0] * len(s)
        i = 0
        while len(s) >= k and i < len(s):
            if i > 0 and s[i] == s[i-1]:
                count[i] = count[i-1] + 1
            else:
                count[i] = 1
            
            if count[i] == k:
                s = s[:i - k + 1] + s[i + 1:]
                i -= k
            else:
                i += 1
        return s

            
            