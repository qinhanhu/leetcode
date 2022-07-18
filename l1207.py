from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        cntSet = set()
        for _, v in counter.items():
            if v not in cntSet:
                cntSet.add(v)
            else:
                return False
        return True