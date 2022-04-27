class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubleS = s + s
        return s in doubleS[1:-1]