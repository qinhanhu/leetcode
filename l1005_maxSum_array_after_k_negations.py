import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        while k > 0:
            _min = heapq.heappop(nums)
            heapq.heappush(nums, -_min)
            k -= 1
        res = 0
        while n > 0:
            res += heapq.heappop(nums)
            n -= 1
        return res