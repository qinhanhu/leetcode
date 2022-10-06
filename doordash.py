#1. L45: https://leetcode.com/problems/jump-game-ii/
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

#2. L1345: https://leetcode.com/problems/jump-game-iv/
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

#3. L721: https://leetcode.com/problems/accounts-merge/
class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.groupCnt = n
        self.parent = [i for i in range(n)]
        # self.groups = {}
        # for i in range(n):
        #     self.groups[i] = set([i])

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV:
            return 
        self.parent[rootV] = rootU
        self.groupCnt -= 1
        # self.groups[rootU].update(self.groups[rootV])
        # del self.groups[rootV]
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAcc = {}
        accToEmail = {}
        n = len(accounts)
        DS = DisjointSet(n)

        for i in range(n):
            accToEmail[i] = []
            for j in range(len(accounts[i])):
                if j > 0:
                    if accounts[i][j] not in emailToAcc:
                        emailToAcc[accounts[i][j]] = i
                    else:
                        DS.union(i, emailToAcc[accounts[i][j]])
                    accToEmail[i].append(accounts[i][j])
        
        # res = []
        # for _, indexSet in DS.groups.items():
        #     indexList = list(indexSet)
        #     name = accounts[indexList[0]][0]
        #     res.append([name])
        #     emails = set()
        #     for i in indexList:
        #         emails.update(accToEmail[i])
        #     res[-1] += sorted(list(emails))
        # return res

        indexToEmail = {}
        for i in range(n):
            parent = DS.find(i)
            if parent not in indexToEmail:
                indexToEmail[parent] = set()
            indexToEmail[parent].update(accToEmail[i])
        
        res = []
        for index, emails in indexToEmail.items():
            name = accounts[index][0]
            res.append([name])
            res[-1] += sorted(list(emails))
        return res

#4. L759: https://leetcode.com/problems/employee-free-time/
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
from sortedcontainers import SortedList
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        1. Sort all intervals by start
        2. merge overlaaping intervals
        3. find gaps
        """
        # sortedlist = SortedList(key=lambda x:x.start)
        n = len(schedule)
        sortedlist = []
        for employee in schedule:
            for interval in employee:
                # sortedlist.add(interval)
                sortedlist.append((interval.start, interval.end))
        sortedlist.sort(key=lambda x: x[0])
        newstart = sortedlist[0][0]
        newend = sortedlist[0][1]
        res = []
        for i in range(1, len(sortedlist)):
            if sortedlist[i][0] <= newend and sortedlist[i][1] > newend:
                newend = sortedlist[i][1]
            elif sortedlist[i][0] > newend:
                res.append(Interval(newend, sortedlist[i][0]))
                newstart = sortedlist[i][0]
                newend = sortedlist[i][1]
        return res

#5. L84:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        1. For height i, find the left and right closest coloumns which are shorter then height[i].(MonoticStack)
        2. Caculate area = height[i] * (right - left - 1)
        i.e. heights = [2,1,5,6,2,3]
             for i = 2, height[2] = 5
             left = 1
             right = 4
             width = right - left - 1 = 2
             height = height[2] = 5
             area = width * height = 10
        """

        # From top to bot, larger to smaller. i.e. height[monoStack[i]] > height[monoStack[i+1]]
        n = len(heights)
        if n < 2:
            return heights[0] if n == 1 else 0
        heights = [0] + heights + [0]
        n = len(heights)
        monoStack = [0]
        area = 0
        for i in range(1, n):
            if heights[i] > heights[monoStack[-1]]:
                monoStack.append(i)
            elif heights[i] == heights[monoStack[-1]]:
                monoStack.append(i)
            else:
                while monoStack and heights[i] < heights[monoStack[-1]]:
                    mid = monoStack.pop()
                    left = monoStack[-1]
                    right = i
                    width = right - left - 1
                    h = heights[mid]
                    area = max(area, width * h)
                monoStack.append(i)

        # # Simplify:
        # for i in range(1, n):
        #     while monoStack and heights[i] < heights[monoStack[-1]]:
        #         mid = monoStack.pop()
        #         left = monoStack[-1]
        #         right = i
        #         width = right - left - 1
        #         h = heights[mid]
        #         area = max(area, width * h)
        #     monoStack.append(i)
        return area

#6. L330: https://leetcode.cn/problems/patching-array/
# Greedy
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        maxRange = 1
        index = 0
        cnt = 0
        # reachable range is [1, maxRange)
        while maxRange <= n:
            if index < len(nums) and maxRange >= nums[index]:
                maxRange += nums[index]
                index += 1
            else:
                cnt += 1
                maxRange = maxRange * 2
        return cnt
        
#7. L532: https://leetcode.cn/problems/k-diff-pairs-in-an-array/
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        1. use a set to store the k-diff pairs
        2. use a hashmap to record numbers already iterated, for current nums[i], see if nums[i] + k  or nums[i] - k
        in the hashmap.
    
        """
        res = set()
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] + k in hashmap:
                res.add((nums[i], nums[i] + k))
            if nums[i] - k in hashmap:
                res.add((nums[i] - k, nums[i]))
            hashmap[nums[i]] = 1
        return len(res)

# 8. L735: https://leetcode.com/problems/asteroid-collision/submissions/
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        use a stack to save the "safe" asteroid
        while iterate asteroids:
            while cur < 0 and stack.top > 0: collisions
        return stack
        """
        n = len(asteroids)
        if n < 2:
            return asteroids
        stack = [asteroids[0]]
        for i in range(1, n):
            curIsSafe = True
            while asteroids[i] < 0 and stack and stack[-1] > 0:
                if -asteroids[i] > stack[-1]:
                    stack.pop()
                elif -asteroids[i] == stack[-1]:
                    stack.pop()
                    curIsSafe = False
                    break
                else:
                    curIsSafe = False
                    break 
            if curIsSafe:
                stack.append(asteroids[i])
        return stack

# 9. L31: https://leetcode.cn/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = n - 2
        j = n - 1
        # 1. find nums[i] < nums[j]
        while i >= 0:
            if nums[i] < nums[j]:
                break
            i -= 1
            j -= 1
        if i >= 0: # if i == -1, j==0. means nums = [3,2,1]
            # 2. in nums[j:], find the nums[x] > nums[i], j <= x <= n - 1
            x = n - 1
            while x >= j:
                if nums[x] > nums[i]:
                    break
                x -= 1
            # swap
            nums[x], nums[i] = nums[i], nums[x]

        # 3. reverse nums[j:]
        left = j
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        
