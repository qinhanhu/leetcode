class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        def helper(arr):
            if len(arr) == 1:
                return
            maxv = 0
            maxindex = 0
            for i, v in enumerate(arr):
                if maxv <= v:
                    maxv = v
                    maxindex = i
            if maxindex < len(arr) - 1:
                arr[:maxindex + 1] = arr[:maxindex + 1][::-1]
                res.append(maxindex+1)
                arr = arr[::-1]
                res.append(len(arr))
            helper(arr[:-1])
        helper(arr)
        return res