class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hmap = {}
        for b in bills:
            if b not in hmap:
                hmap[b] = 1
            else:
                hmap[b] += 1
                
            change = b - 5
            if change == 0:
                continue
            elif change == 5:
                if 5 in hmap and hmap[5]> 0:
                    hmap[5] -= 1
                else:
                    return False
            elif change == 15:
                if 10 in hmap and 5 in hmap and hmap[10] >= 1 and hmap[5] >= 1:
                    hmap[10] -= 1
                    hmap[5] -= 1
                elif 5 in hmap and hmap[5] >= 3:
                    hmap[5] -= 3
                else:
                    return False
        return True
                
