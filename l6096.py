import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        n = len(potions)
        for s in spells:
            cnt = 0
            target = success / s
            if target > potions[-1]:
                res.append(cnt)
                continue
            # left = 0
            # right = n - 1
            # while left < right:
            #     mid = (right - left) // 2 + left
            #     if potions[mid] == target:
            #         left = mid
            #         break
            #     if potions[mid] < target:
            #         left = mid+1
            #     else:
            #         right = mid-1
            # cnt = n - left + 1
            i = bisect.bisect_left(potions, target)
            cnt = n - i
            res.append(cnt)
            
                
        return res