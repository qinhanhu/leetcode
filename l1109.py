class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diffs = [0] * n
        for book in bookings:
            left = book[0] - 1
            right = book[1] - 1
            value = book[2]
            diffs[left] += value
            if right < n - 1:
                diffs[right + 1] -= value
        res = []
        preSum = 0
        for i in range(n):
            preSum += diffs[i]
            res.append(preSum)
        return res
        