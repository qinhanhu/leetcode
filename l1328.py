class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <= 1:
            return ""
        
        mid = n // 2
        res = list(palindrome)
        for i in range(n):
            if i <= mid - 1 and res[i] > 'a':
                res[i] = 'a'
                break
            elif i >= mid:
                res[-1] = 'b'
                break
                    
        return "".join(res)