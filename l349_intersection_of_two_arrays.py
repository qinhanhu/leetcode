class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        hashmap = {}
        for i in nums1:
            hashmap[i] = 1
        for i in nums2:
            if i in hashmap:
                res.add(i)
        return list(res)