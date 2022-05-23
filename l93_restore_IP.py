class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.maxDepth = 4

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        def backtracking(s: str, startIndex: int):
            if len(self.path) > self.maxDepth:
                return
            if startIndex == len(s) and len(self.path) == self.maxDepth:
                self.res.append(".".join(self.path))
                return
            
            for i in range(startIndex, len(s)):
                if self.isLeadingZero(s[startIndex:i+1]):
                    return
                if i - startIndex + 1 > 3:
                    return
                if int(s[startIndex:i+1]) > 255:
                    return
                self.path.append(s[startIndex:i+1])
                backtracking(s, i+1)
                self.path.pop()
        
        backtracking(s, 0)
        return self.res

    def isLeadingZero(self, s:str):
        if s == "0":
            return False
        elif s[0] == "0":
            return True
        return False
