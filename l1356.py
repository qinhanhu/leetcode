class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda a: (self.countOnes(a), a))
        return arr
    def countOnes(self, n: int):
        cnt = 0
        while n:
            n &= n-1
            cnt += 1
        return cnt