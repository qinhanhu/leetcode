class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return 1
        points.sort(key=lambda x: x[0])
        cnt = 1
        for i in range(1, n):
            if points[i][0] > points[i-1][1]:
                cnt += 1
            else:
                points[i][1] =  min(points[i][1], points[i-1][1])
        return cnt 