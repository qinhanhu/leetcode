class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n < 2:
            return 0
        intervals.sort()
        # print(intervals)
        cnt = 0
        for i in range(1, n):
            if intervals[i][0] < intervals[i-1][1]:
                cnt += 1
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
        return cnt