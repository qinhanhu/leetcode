import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        heap = []
        for num, cnt in hmap.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, num))
            elif cnt > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (cnt, num))
        res = []
        for item in heap:
            res.append(item[1])
        return res