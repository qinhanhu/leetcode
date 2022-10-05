# L45: https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy: For i-th jumb, we iterate from index(i) to index(i+nums[i]), 
        # which is the farthest index(maxRange) we can reach for now. 
        # Meanwhile, update the farthest index we can reach untill maxRange == n - 1.
        
        n = len(nums)
        if n < 2:
            return 0
        
        maxRange = nums[0]
        cur = 0
        step = 1
        
        while maxRange < n - 1:
            for i in range(cur, maxRange + 1):
                maxRange = max(maxRange, i + nums[i])
                cur += 1
            step += 1
        return step

# L1345: https://leetcode.com/problems/jump-game-iv/
from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        BFS: 1. Using hashmap to store indexes with same value.
             2. Start BFS from the first index: enque all nodes that can be reached in one step.
             3. If reaching the last node, return.
             4. Record visited nodes. 
        """
        n = len(arr)
        if n < 2:
            return 0
        neighbors = {}
        for i, v in enumerate(arr):
            if v not in neighbors:
                neighbors[v] = []
            neighbors[v].append(i)
        queue = deque()
        queue.append(0)
        steps = 0
        visited = set()
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                visited.add(cur)
                if cur == n - 1:
                    return steps
                if cur + 1 < n and cur + 1 not in visited:
                    queue.append(cur+1)
                if cur - 1 >= 0 and cur - 1 not in visited:
                    queue.append(cur-1)
                if arr[cur] in neighbors:    
                    for index in neighbors[arr[cur]]:
                        if index not in visited:
                            queue.append(index)
                    neighbors[arr[cur]].clear()
            steps += 1