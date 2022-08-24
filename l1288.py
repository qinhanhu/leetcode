class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return n  
        intervals.sort(key=lambda x: (x[0], -x[1]))
        _min = intervals[0][0]
        _max = intervals[0][1]
        res = n
        for i in range(1, n):
            left = intervals[i][0]
            right = intervals[i][1]
            if _min <= left and _max >= right:
                res -= 1
            elif right >= _max:
                _max = right
        return res