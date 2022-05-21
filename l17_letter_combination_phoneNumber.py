class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(digits, index):
            if len(self.path) == len(digits):
                self.res.append("".join(self.path[:]))
                return
            letters = self.hashmap[digits[index]]
            for i in range(len(letters)):
                self.path.append(letters[i])
                backtracking(digits, index+1)
                self.path.pop()
        
        if not digits:
            return []
        backtracking(digits, 0)
        return self.res

