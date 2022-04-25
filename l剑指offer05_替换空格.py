class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        res = ""
        for ch in s:
            if ch == ' ':
                res += "%20"
            else:
                res += ch
        return res