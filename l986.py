class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        res = []
        while first < len(firstList) and second < len(secondList):
            starti = firstList[first][0]
            endi = firstList[first][1]
            startj = secondList[second][0]
            endj = secondList[second][1]
            if starti <= endj and startj <= endi:
                res.append([max(starti, startj), min(endi, endj)])
            
            if endj < endi:
                second += 1
            else:
                first += 1
        return res