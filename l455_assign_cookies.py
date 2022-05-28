class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gindex = 0
        for i in range(len(s)):
            if gindex < len(g) and s[i] >= g[gindex]:
                gindex += 1
            
        return gindex
