class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peek = 0
        predif = arr[1] - arr[0]
        if predif < 0 :
            return False
        for i in range(2, len(arr)):
            dif =  arr[i] - arr[i - 1]
            if dif == 0:
                return False
            if predif * dif < 0:
                peek += 1
            predif = dif
        return peek == 1