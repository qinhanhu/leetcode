import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        
        for i in range(1, len(heights)):
            dif = heights[i] - heights[i-1]
            if dif > 0:
                heapq.heappush(minHeap, dif)
                if len(minHeap) > ladders:
                    bricks -= heapq.heappop(minHeap)
                    if bricks < 0:
                        return i-1
                    
        return len(heights) - 1
            
            
            
        
        
    
        
        