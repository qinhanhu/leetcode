class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        r, c = rStart, cStart
        deltar, deltac = 0, 1
        rotateCnt = 0
        step = 1
        
        while len(res) < rows * cols:
            if 0 <= r <= rows - 1 and 0 <= c <= cols - 1:
                res.append((r, c))
            
            if r + deltar > rStart + step or r + deltar < rStart - step or c + deltac > cStart + step or c + deltac < cStart - step:
                if rotateCnt == 4:
                    step += 1
                    rotateCnt = 0
                else:
                    deltar, deltac = deltac, -deltar
                    rotateCnt += 1
            
            r += deltar
            c += deltac
        return res
                    
            
        