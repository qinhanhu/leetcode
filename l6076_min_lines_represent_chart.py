class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) < 2:
            return 0
        stockPrices = sorted(stockPrices, key=lambda x: x[0])
        res = 1
        preDeltaY = stockPrices[1][1] - stockPrices[0][1]
        preDeltaX = stockPrices[1][0] - stockPrices[0][0]
        for i in range(1, len(stockPrices) - 1):
            curDeltaY = stockPrices[i+1][1] - stockPrices[i][1]
            curDeltaX = stockPrices[i+1][0] - stockPrices[i][0]
            if preDeltaY * curDeltaX != curDeltaY * preDeltaX:
                res += 1
            preDeltaY = curDeltaY
            preDeltaX = curDeltaX
        return res