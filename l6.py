class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        res = []
        for _ in range(numRows):
            res.append("")
        
        deltaIndex = -1
        index = 0
        for ch in s:
            if index == 0 or index == numRows - 1:
                deltaIndex = -deltaIndex
            res[index] += ch
            index += deltaIndex
        return "".join(res)
        
