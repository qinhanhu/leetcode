class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sumMap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in sumMap:
                    sumMap[n1 + n2] += 1
                else:
                    sumMap[n1 + n2] = 1
        
        res = 0
        for n3 in nums3:
            for n4 in nums4:
                if (0 - n3 - n4) in sumMap:
                    res += sumMap[0 - n3 - n4]
        return res