class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        def reverse(s: list, start, end: int):
            left, right = start, end
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        mutableStr = list(s.strip())
        start, end = 0, len(mutableStr) - 1
        reverse(mutableStr, start, end)
        reverse(mutableStr, start, len(mutableStr) - n - 1)
        reverse(mutableStr, len(mutableStr) - n, end)
        return "".join(mutableStr)