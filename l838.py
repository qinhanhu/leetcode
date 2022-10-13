class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        we have 4 cases:
        L...L -> LLLLL
        L...R -> L...R
        R...R -> RRRR
        R...L -> RR.LL or RRRLLL
        
        idea:
        1. Add fake head and tail char that is dominoes = "L" + dominoes + "R"
        2. Use two pointers l and r, matches the 4 cases above, then update final states to result.
        
        Time: O(n)
        Space: O(n)
        """
        dominoes = "L" + dominoes + "R"
        l = 0
        r = 1
        res = ""
        n = len(dominoes)
        while r < n:
            if dominoes[r] != ".":
                if l > 0:
                    res += dominoes[l]
                size = r - l - 1
                if dominoes[l] == dominoes[r] == "L":
                    res += "L" * size
                elif dominoes[l] == dominoes[r] == "R":
                    res += "R" * size
                elif dominoes[l] == "L" and dominoes[r] == "R":
                    res += "." * size
                else:
                    # R...L -> RR.LL or RRRLLL
                    res += "R" * (size // 2) + "." * (size % 2) + "L" * (size // 2)
                l = r
            r += 1
        return res
        
        

        