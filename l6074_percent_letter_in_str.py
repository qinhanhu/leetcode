class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = 0
        for i in s:
            if i == letter:
                cnt += 1
        return cnt * 100 // len(s)