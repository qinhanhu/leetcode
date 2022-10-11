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

# 10. L559: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # BFS
        if not root:
            return 0
        que = deque()
        que.append(root)
        level = 0
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                for child in cur.children:
                    que.append(child)
            level += 1
        return level

# 11. L859: https://leetcode.com/problems/buddy-strings/
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n, m = len(s), len(goal)
        if n != m:
            return False
        if s == goal:
            return len(set(s)) < m
        
        diffIx = []
        for i in range(n):
            if s[i] != goal[i]:
                diffIx.append(i)
        if len(diffIx) != 2:
            return False
        if s[diffIx[0]] == goal[diffIx[1]] and s[diffIx[1]] == goal[diffIx[0]]:
            return True
        return False
        
# 12. L1347
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hmap = [0] * 26
        n = len(s)
        for i in range(n):
            hmap[ord(s[i]) - ord('a')] += 1
        for j in range(n):
            hmap[ord(t[j]) - ord('a')] -= 1
        
        res = 0
        for cnt in hmap:
            if cnt > 0:
                res += cnt
        return res

# 13. L854: https://leetcode.cn/problems/k-similar-strings/
from collections import deque
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # BFS
        n = len(s2)
        k = 0
        que = deque()
        que.append(s1)
        visited = set()
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                visited.add(cur)
                if cur == s2:
                    return k
                i = 0
                while cur[i] == s2[i]:
                    i += 1
                for j in range(i+1, n):
                    if cur[j] == s2[i] and cur[j] != s2[j]:
                        temp = list(cur)
                        temp[i], temp[j] = temp[j], temp[i]
                        temp = "".join(temp)
                        if temp not in visited:
                            que.append(temp)
            k += 1
        return -1
        
# 14. L36
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet, colSet, blockSet = [], [], []
        for _ in range(9):
            rowSet.append([0] * 9)
            colSet.append([0] * 9)
            blockSet.append([0] * 9)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                val = int(board[i][j]) - 1
                if rowSet[i][val]:
                    return False
                if colSet[j][val]:
                    return False
                if blockSet[int(i / 3) * 3 + int(j / 3)][val]:
                    return False
                
                rowSet[i][val] += 1
                colSet[j][val] += 1
                blockSet[int(i / 3) * 3 + int(j / 3)][val] += 1
        return True

# 15. L37
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtracking(board) -> bool:
            rowsLen = colsLen = 9
            for i in range(rowsLen):
                for j in range(colsLen):
                    if board[i][j] != '.':
                        continue
                    for val in range(1, 10):
                        if not isValid(i, j, str(val), board):
                            continue
                        board[i][j] = str(val)
                        if backtracking(board) is True:
                            return True
                        board[i][j] = '.'
                    return False
            return True
                        
        def isValid(row, col, val, board) -> bool:
            rowsLen = colsLen = 9
            # same row
            for j in range(colsLen):
                if board[row][j] == val:
                    return False
            # same col
            for i in range(rowsLen):
                if board[i][col] == val:
                    return False
            # 3 * 3
            startRow = int(row / 3) * 3
            startCol = int(col / 3) * 3
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == val:
                        return False
            return True

        backtracking(board)
        return

# 16. L124
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = -float("inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        n
        |
        a
      /   \
     b     c
     
     for node a, 
     1. b -> a -> c may be maxSum, update maxSum
     2. b -> a -> a.parent 
     3. c -> a -> a.parent 
     return max(path(b->a, c->a)) to a.parent
        """
        self.dfs(root)
        return self.maxSum
        
    def dfs(self,root) -> int:
        if not root:
            return 0
        
        leftMax = max(0, self.dfs(root.left))
        rightMax = max(0, self.dfs(root.right))

        self.maxSum = max(self.maxSum, root.val + leftMax + rightMax)
        return max(root.val, leftMax + root.val, rightMax + root.val)

# 17. L210
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        topological sort
        """
        # step1: create graph and indegree map
        # prerequisites[i] = [ai, bi] represents edge (bi -> ai)
        # graph is a map(K, V), K is a node and V is nodes it can reach
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for dst, src in prerequisites:
            graph[src].append(dst)
            indegree[dst] += 1
        
        # step 2: BFS from every node with 0 indegree.
        que = deque()
        for i, val in enumerate(indegree):
            if val == 0:
                que.append(i)
        visited = 0
        res = []
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                res.append(cur)
                for neighbors in graph[cur]:
                    indegree[neighbors] -= 1
                    if indegree[neighbors] == 0:
                        que.append(neighbors)
            visited += size
        # Find Loop
        if visited != numCourses:
            return []
        return res

# 18. L286: https://leetcode.com/problems/walls-and-gates/
# https://leetcode.com/discuss/interview-question/1522955/Doordash-Onsite
def wallsAndGates(rooms):
    """
    Do not return anything, modify rooms in-place instead.
    """
    """
    BFS from all gates at the same time
    Time: O(mn)
    Space: O(mn) queue's size

    follow up是 如果每个customer都去离自己最近的mart，
    要找出每一个DashMart serve customers的数量。
    只需要在BFS时记录customer会去哪个mart, 这个结果会传递给下一轮BFS.
    同时martToCustomers[mart] += 1
    
    """
    INF = 2**31 - 1
    queue = collections.deque()
    m = len(rooms)
    n = len(rooms[0])
    visited = set()
    martToCustomers = {}
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j, (i,j)))
                visited.add((i, j))
                martToCustomers[(i, j)] = 0

    
    distance = 0
    while len(queue) > 0:
        size = len(queue)
        for _ in range(size):
            i, j, mart = queue.popleft()
            if rooms[i][j] == INF:
                martToCustomers[mart] += 1
                rooms[i][j] = distance
            for nexti, nextj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= nexti <= m-1 and 0 <= nextj <= n-1 and rooms[nexti][nextj] == INF and (nexti, nextj) not in visited:
                    queue.append((nexti, nextj, mart))
                    visited.add((nexti, nextj))
        distance += 1

    print(martToCustomers)

# wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])


# 19. L289: https://leetcode.cn/problems/game-of-life/
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Rules: 
        live = 1 dead = 0
        live -> dead: 3
        dead -> live: 2
        live -> live: 1
        dead -> dead: 0
        
        if neighbor % 2 == 0: 
            neighbor is dead
        else: 
            neighbor is live
            
        Time: O(mn)
        Space: O(1) in place
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                starti = max(0, i-1)
                endi = min(m-1, i+1)
                startj = max(0, j-1)
                endj = min(n-1, j+1)
                liveNeighbors = 0
                for x in range(starti, endi+1):
                    for y in range(startj, endj+1):
                        if x == i and y == j:
                            continue
                        if board[x][y] % 2 != 0:
                            liveNeighbors += 1
                if board[i][j] == 1:
                    # live -> dead
                    if liveNeighbors != 2 and liveNeighbors != 3:
                        board[i][j] = 3
                else:
                    # dead -> live
                    if liveNeighbors == 3:
                        board[i][j] = 2
        # restore board: 3 -> 0, 2 -> 1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


# 20. L297: https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.serializeHelper(root, res)
        return ",".join(res)
    
    def serializeHelper(self, root, res:list) -> None:
        if not root:
            res.append("None")
            return
        res.append(str(root.val))
        self.serializeHelper(root.left, res)
        self.serializeHelper(root.right, res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = collections.deque(data.split(","))
        return self.deserializeHelper(data)
    
    def deserializeHelper(self, que) -> 'TreeNode':
        val = que.popleft()
        if val == "None":
            return None
        node = TreeNode(int(val))
        node.left = self.deserializeHelper(que)
        node.right = self.deserializeHelper(que)
        return node
            
# 21. L428
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    # def __init__(self):
    #     self.res = ""
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = []
        self.serializeHelper(root, res)
        return ",".join(res)
    def serializeHelper(self, root, res:list):
        if not root:
            return ""
        res.append(str(root.val))
        res.append(str(len(root.children)))
        for child in root.children:
            self.serializeHelper(child, res)
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        data = collections.deque(data.split(","))
        return self.deserializeHelper(data)
    def deserializeHelper(self, data):
        if len(data) < 1:
            return None
        val = data.popleft()
        node = Node(int(val), [])
        size = int(data.popleft())
        for _ in range(size):
            node.children.append(self.deserializeHelper(data))
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# 22. L317
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        1. for every building, 
           get shortest travel distances between the building with every empty land.      (using BFS)
           
           i.e. we can get
                STDfromB1 = [m * n]
                STDfromB2 = [m * n]
                STDfromB3 = [m * n]
        2. Iterate empty land (i, j), 
           find min(STDfromB1[i,j] + STDfromB2[i,j] + STDfromB3[i,j])
        """
        # find bulidings
        m = len(grid)
        n = len(grid[0])
        buildings = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append((i, j))
                
        STDs = []
        for start in buildings:
            STD, flag = self.bfs(grid, start)
            if not flag:
                return -1
            STDs.append(STD)
        _min = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    _sum = 0
                    for x in range(len(STDs)):
                        _sum += STDs[x][i][j]
                    _min = min(_min, _sum)
        return _min if _min != float('inf') else -1
            
    def bfs(self, graph, start):
        que = collections.deque()
        que.append(start)
        distance = 0
        m = len(graph)
        n = len(graph[0])
        STD = []
        for i in range(m):
            STD.append([float('inf')] * n)
        visited = set()
        visited.add(start)
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                STD[i][j] = distance
                for nexti, nextj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= nexti <= m-1 and 0 <= nextj <= n-1 and (nexti,nextj) not in visited and graph[nexti][nextj] == 0:
                        que.append((nexti, nextj))
                        visited.add((nexti, nextj))
            distance += 1
        return STD, len(visited) > 1

# 23. L329: https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Input: matrix: List[List[int]]
        Output: int: the length of Longest Increasing path
        We can start/end from/to any position in the matrix.
        
        case:
            9 9 4
            6 6 8
            2 1 1  the output is 4, path could be [1, 2, 6, 9]
            
        idea: 
        1. step1: do BFS for every node(m * n) 
                    and use a variable to record the max steps the BFS can reach.
                    return the variable
            Time: O((mn)^2)
            Space: need a queue for bfs, which is O(m * n)

        Observation: for node 1: we traverse and get [1, 2, 6, 9], 
            and when we do bfs for node 2, we traverse and get [2, 6, 9]
            if start 9, we get [9]
            then start 6, we get[6, res(9)]
            ..2 [2,res(6)]
            ..1 [1, res(2)]
        
        2. do BFS start from nodes with biggest value and forward by decreasing path
           i.e. [9, 6, 2, 1]
           which we could use Topological Sort algo:
           For this case: 
           1. build outdegree map: iterate every node, if node A's neighbor B is bigger, 
           link edge A -> B which means outdegree[A] += 1
            graph:  9 9<4
                    ^ ^ v         
                    6 6>8
                    ^ ^ ^
                    2<1 1
            2. enqueue nodes with 0 outdegree
            3. pop node from queue and decrease the outdgree of its neighbours. Update the num of level(depth) we reach.
            repeat 2&3 untill queue be empty and return the depth.
            Time: O(MN) each node only need to be visited once
            Space: O(MN) the queue size
        """
        m = len(matrix)
        n = len(matrix[0])
        #1. build outdegree map(step1,2)
        outdegree = dict()
        que = collections.deque()
        for i in range(m):
            for j in range(n):
                outdegree[(i,j)] = 0
                for nexti, nextj in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= nexti <= m-1 and 0<=nextj<=n-1 and matrix[i][j] < matrix[nexti][nextj]:
                        # graph[(i,j)].add((nexti, nextj))
                        outdegree[(i,j)] += 1
                if outdegree[(i, j)] == 0:
                    que.append((i, j))
        # BFS step3
        res = 0
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                for nexti, nextj in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= nexti <= m-1 and 0<=nextj<=n-1 and matrix[i][j] > matrix[nexti][nextj]:
                        outdegree[(nexti, nextj)] -= 1
                        if outdegree[(nexti, nextj)] == 0:
                            que.append((nexti, nextj))
            res += 1
        return res

# 24. LC341
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # self.nestedList = collections.deque(nestedList)
        self.stack = nestedList[::-1]
        
        
    def next(self) -> int:
        # return self.nestedList.popleft()
        return self.stack.pop()
        
    def hasNext(self) -> bool:
        # while self.nestedList:
        #     item = self.nestedList[0]
        #     if item.isInteger() is True:
        #         return True
        #     item = self.nestedList.popleft()
        #     item = item.getList()
        #     for i in range(len(item) - 1, -1, -1):
        #         self.nestedList.appendleft(item[i])
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            top = self.stack.pop().getList()
            top = top[::-1]
            self.stack += top
        return False
        
         
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
