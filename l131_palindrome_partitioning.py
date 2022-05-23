class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    def partition(self, s: str) -> List[List[str]]:
        def backtracking(s, startIndex):
            if startIndex == len(s):
                self.res.append(self.path[:])
                return
            
            for i in range(startIndex, len(s)):
                # print(s[startIndex:i+1], i)
                if not self.isPalindrome(s[startIndex:i+1]):
                    # print(s[startIndex:i+1])
                    continue
                self.path.append(s[startIndex:i+1])
                backtracking(s, i+1)
                self.path.pop()

        backtracking(s, 0)
        return self.res    

        
    def isPalindrome(self, s:str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True