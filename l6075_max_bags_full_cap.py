class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        remain = []
        for i in range(n):
            remain.append(capacity[i] - rocks[i])
        remain.sort()
        cnt = 0
        for i in remain:
            additionalRocks -= i
            if additionalRocks < 0:
                break
            cnt += 1
        return cnt
        