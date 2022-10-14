import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        while left < right:
            speed = left + (right - left) // 2
            timeNeeded = 0
            for p in piles:
                timeNeeded += math.ceil(p / speed)
            # too slow -> improve speed
            if timeNeeded > h:
                left = speed + 1
            else:
                right = speed
        return left

                

