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
"""
# Definition: Similar restaurants
# Two restaurants R1 and R2 are similar if we can swap a maximum of two letters (in different positions) of R1, so that it equals R2.
# For example, source one may have a restaurant named "omega grill" while another source may have the same restaurant as "omgea grill".
# For example, "biryani" and "briyani" are similar (swapping at positions 1 and 2). 
    "biryani" is not similar to following, "biryeni" (no e to swap with), "briynai"(Needs 2 swap)
# For a given restaurant name, find and return all the similar restaurant names in the list.
"""
def similarRestaurants(name: str, restaurants: list[str]) -> list[str]:
    """
    idea:
    1. len(R1) == len(R2)
    2. R1 contains the same chrs with R2
    3. SWAP only once: R1:  ...a....b...
                        R2: ...b....a...
        we do one swap, and see whether R1 == R2
    """
    res = []
    for restaurant in restaurants:
        if buddyStrings(name, restaurant):
            res.append(restaurant)
        else:
            res.append("")
    return res


# 12. L1347: https://leetcode.cn/problems/minimum-number-of-steps-to-make-two-strings-anagram/
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

"""
follow up:，一个string到另一个string，每次换字母要把所有的同一个字母都换了，比如说a换c要把string里面的a全都换成c，不能只换一个a。
然后换n次之后，如果两个string是anagram，我们称这两个string同属于一个n阶anagram group，求的是如果给任意两个string和k，判断这两个string是否同属于k阶anagram group。也就是说，一个string能否通过k次变换，成为另一个string的anagram。
例子1：string1: anagram。string2: cnagrcy。k：2。输出：true
过程：cnagrc‍‌ -> anagray -> anagram
例子2: string1: anagram string2: cxagrcm。k：1。输出：false
"""
def followup(str1, str2, k) -> bool:
    """
    求str1比str2多的字符->map1 和 str2比str1多的字符->map2, 
    需要满足len(map1) == len(map2) == k（题目要求必须交换k次）且 两个map的key值拿出来排序的结果相等.
    case: anagram 比 cnagrcy 多 {a:2, m:1}, cnagrcy比anagram 多{c:2, y:1}
    """
    if len(str1) != len(str2):
        return False
    diffMap = [0] * 26
    for ch in str1:
        diffMap[ord(ch) - ord('a')] += 1
    for ch in str2:
        diffMap[ord(ch) - ord('a')] -= 1
    str1Remain = []
    str2Remain = []
    for num in diffMap:
        if num > 0:
            str1Remain.append(num)
        elif num < 0:
            str2Remain.append(-num)
    str1Remain.sort()
    str2Remain.sort()      
    return str1Remain == str2Remain and len(str1Remain) == k

# print(followup("anagram", "cnagrcy", 2))
# print(followup("anagram", "cxagrcm", 1))
# print(followup("anagram", "cxagrcm", 2))

"""
K-anagram
# Given a restaurant name, find other restaurants in the list that are k-anagrams with each other. 
A name is a k-anagram with another name if both the conditions below are true:
# The names contain the same number of characters.
# The names can be turned into anagrams by changing at most k characters in the strin‍‌g
# For example:
# name = "grammar", k = 3 and list = ["anagram"], "grammar" is k-anagram with "anagram" 
since they contain the same number of characters and you can change 'r' to 'n' and 'm' to 'a'.
# name = "omega grill", k = 2 and list = ["jmega frill"], "omega grill" is k-anagram with "jmega frill" 
since they contain same number of characters and you can change 'o' to 'j' and 'g' to 'f'
"""
def k_anagram(name, restaurants:list) -> list:
    """
    constraint:
    do R1 and R2 only consist of lowercase letters "a-z"?
    time: O(N) N is the num of characters
    space: O(n*len(name))
    """
    res = []
    for item in restaurants:
        if isKanagram(name, item):
            res.append(item)
        else:
            res.append("")

def isKanagram(str1, str2) -> bool: # - O(n)
    if len(str1) != len(str2):
        return False
    chToCnt = dict()
    for ch in str1:
        if ch not in chToCnt:
            chToCnt[ch] = 0
        chToCnt[ch] += 1
    for ch in str2:
        if ch not in chToCnt:
            chToCnt[ch] = 0
        chToCnt[ch] -= 1
    diff = 0
    for k,v in chToCnt.items():
        if v > 0:
            diff += 1
    return diff <= k




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
def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    """
    BFS from all gates at the same time
    Time: O(mn)
    Space: O(mn) queue's size
    
    """
    INF = 2**31 - 1
    queue = collections.deque()
    m = len(rooms)
    n = len(rooms[0])
    visited = set()
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j))
                visited.add((i, j))
    
    distance = 0
    while len(queue) > 0:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()
            rooms[i][j] = distance
            for nexti, nextj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= nexti <= m-1 and 0 <= nextj <= n-1 and rooms[nexti][nextj] == INF and (nexti, nextj) not in visited:
                    queue.append((nexti, nextj))
                    visited.add((nexti, nextj))
        distance += 1

    """
    Follow up，大概是：现在地图上‍‌还多了些customers 'C'，
    离他最近的dashmart应该serve他，如果两个D离他距离一样那都可以serve他，
    输出每个D可以serve的customer数量 / 输出serve customer最多的那个dashmart。
    改变BFS入队条件即可
    """
def wallsAndGates(rooms):
    """
    Do not return anything, modify rooms in-place instead.
    """
    """
    BFS from all gates at the same time
    Time: O(mn)
    Space: O(mn) queue's size
    """
    INF = 2**31 - 1
    queue = collections.deque()
    m = len(rooms)
    n = len(rooms[0])
    martToCustomers = {}
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j, (i,j)))
                martToCustomers[(i, j)] = 0
    
    distance = 0
    while len(queue) > 0:
        size = len(queue)
        for _ in range(size):
            i, j, mart = queue.popleft()
            if rooms[i][j] != 0 and rooms[i][j] >= distance:
                martToCustomers[mart] += 1
                rooms[i][j] = distance
            for nexti, nextj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= nexti <= m-1 and 0 <= nextj <= n-1:
                    if rooms[nexti][nextj] >= distance + 1:
                        queue.append((nexti, nextj, mart))
        distance += 1
    print(martToCustomers)



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

# 25. LC463
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for nexti, nextj in [(i, j+1),(i, j-1),(i+1, j), (i-1, j)]:
                        if 0<=nexti<=m-1 and 0<=nextj<=n-1 and grid[nexti][nextj] == 1:
                            continue
                        res += 1
        return res

# 26. LC1166: https://leetcode.com/problems/design-file-system/
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.value = 0
        
class FileSystem:

    def __init__(self):
        self.root = Trie()

    def createPath(self, path: str, value: int) -> bool:
        if len(path) <= 1:
            return False
        cur = self.root
        dictionarys = path.split("/")[1:]
        for i, dicName in enumerate(dictionarys):
            # parent dic not exists
            if i != len(dictionarys) - 1 and dicName not in cur.children:
                return False       
            cur = cur.children[dicName]
            if i == len(dictionarys) - 1:
                # already exists
                if cur.value != 0:
                    return False
                cur.value = value
        return True
        

    def get(self, path: str) -> int:
        cur = self.root
        dictionarys = path.split("/")[1:]
        for i, dicName in enumerate(dictionarys):  
            if dicName not in cur.children:
                return -1
            cur = cur.children[dicName]
        return cur.value
            
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# 27. LC588: https://leetcode.com/problems/design-in-memory-file-system/
class Trie:
    def __init__(self, name=""):
        self.children = collections.defaultdict(Trie)
        self.content = ""
        self.name = name
        
class FileSystem:

    def __init__(self):
        self.root = Trie()
        
    def ls(self, path: str) -> List[str]:
        cur = self.root
        if len(path) > 1: # not "/"
            path = path.split("/")[1:]
            for i, dicName in enumerate(path):
                if dicName not in cur.children:
                    return []
                cur = cur.children[dicName]
        res = []
        # directory path
        if not cur.content:
            for name in cur.children.keys():
                res.append(name)
            res.sort()
        else:
            # file path
            if cur.name:
                res.append(cur.name)
        return res

    def mkdir(self, path: str) -> None:
        cur = self.root
        path = path.split("/")[1:]
        for dicName in path:
            cur = cur.children[dicName]
            cur.name = dicName

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")[1:]
        cur = self.root
        for dicName in path:
            cur = cur.children[dicName]
            cur.name = dicName
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split("/")[1:]
        cur = self.root
        for dicName in path:
            if dicName not in cur.children:
                return ""
            cur = cur.children[dicName]
        return cur.content
        
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)


# 28. L642: https://leetcode.com/problems/design-search-autocomplete-system/
"""
Note: SortedList 直接更新排序key的值不会动态更新排序,要先del key,再add.

idea:
Trie to store relationship between prefix and sentences
i.e. sentences = ["i love", "island"]
Trie: {"root": 
            {"i": 
                {" ":
                    {"l":
                        {"o":
                            {"v":
                                {"e",
      }}}}}}}
so if node is "i", node.children = Trie{" ":{..}, "s":{..}}
                   node.prefixs = [("i love", 5), ("island", 3)]
    so if inputStr is  "i", we traverse through Trie,
    we can get top 3 hot sentences from node.prefixs
    if user finished input, i.e. inputStr = "i like#"
    we also need traverse Trie and add/update "i like" to all curNode.prefix sorted list.

"""
import collections
from sortedcontainers import SortedList
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.prefixs = SortedList(key=lambda x:(-x[1], x[0]))
        # self.prefixs = []
class AutocompleteSystem:

    def __init__(self, sentences: list[str], times: list[int]):
        self.topK = 3
        self.inputStr = ""
        self.root = Trie()
        for i,word in enumerate(sentences):  # O(N)
            cur = self.root
            for ch in word:
                cur = cur.children[ch]
                cur.prefixs.add([word, times[i]])       # O(logn)
                # cur.prefixs.append([word, times[i]])
                # cur.prefixs.sort(key=lambda x:(-x[1], x[0]))
        
    def input(self, c: str) -> list[str]:
        cur = self.root
        # finish input, update historial sentence
        if c == "#":
            for ch in self.inputStr: # O(N)
                cur = cur.children[ch]
                find = False
                for i, (prefix, time) in enumerate(cur.prefixs): # O(n)
                    if prefix == self.inputStr:
                        find = True
                        # cur.prefixs[i][1] += 1
                        # cur.prefixs.sort(key=lambda x:(-x[1], x[0]))
                        del cur.prefixs[i]
                        cur.prefixs.add([prefix, time + 1])     # O(logn)
                if not find:
                    cur.prefixs.add([self.inputStr, 1])
                    # cur.prefixs.append([self.inputStr, 1])
                    # cur.prefixs.sort(key=lambda x:(-x[1], x[0]))
            # print(cur.prefixs)
            self.inputStr = ""
            return []
        
        self.inputStr += c
        for ch in self.inputStr:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]
        # print(cur.prefixs)
        res = []
        for prefix, _ in cur.prefixs[:3]:
            res.append(prefix)
        return res


# 29. LC778: https://leetcode.cn/problems/swim-in-rising-water/
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        input: grid is list[list[int]], grid[i][j] >= 0
        output: int, the least time needed to reach (n-1,n-1) from (0,0)
        
        idea:
        Similar to Dijkstra Algo, 
        1. we start BFS from (0,0) and use Priority Queue(minHeap) to update nodes that can be reached,
        2. every step we chose the node with the lowest elevation from candidate nodes.
        3. record and update the max elevation on the nodes we passed.

        Time: O(n^2logn)
        Space: O(n^2) size of minHeap
        """
        # time needed to reach (i, j) ffrom start
        n = len(grid)
        timeFromStart = []
        for i in range(n):
            timeFromStart.append([n*n] * n)
        timeFromStart[0][0] = 0
        minHeap = []
        # heap[(value, (x,y))]
        heapq.heappush(minHeap, (grid[0][0], (0,0)))
        res = -1
        while len(minHeap) > 0:
            cur = heapq.heappop(minHeap)
            val = cur[0]
            node = cur[1]
            i, j = node[0], node[1]
            res = max(res, val)
            if i == n-1 and j == n-1:
                break
            for nexti, nextj in [(i,j+1), (i,j-1), (i+1, j), (i-1, j)]:
                if 0<=nexti<=n-1 and 0<=nextj<=n-1 and grid[nexti][nextj] < timeFromStart[nexti][nextj]:
                    timeFromStart[nexti][nextj] = grid[nexti][nextj]
                    heapq.heappush(minHeap, (grid[nexti][nextj], (nexti, nextj)))
        return res

# 30. L826: https://leetcode.cn/problems/most-profit-assigning-work/
"""
for worker[i], we need to find the maxProfit when the difficulty interval falls [1, work[i]]
1. sort (difficulty, profix)
2. sort worker
3. iterate worker, res += maxProfit
Time: O(nlogn + mlogm) sort
Space: O(n) jobs
"""
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        res = 0
        i = 0
        preMax = 0
        worker.sort()
        for work in worker:
            while i < len(jobs) and work >= jobs[i][0]:
                if jobs[i][1] >= preMax:
                    preMax = jobs[i][1]
                i += 1

            res += preMax
        return res
"""
Followup：假设skill和difficulty都是1-100的整数‍‌，要求用O(M+N)的时间
1. use a int[101] array A to record the maxProfit, A[i] means the maxProfit when difficulty <= i
2. for worker[i], res += A[i]

Time: O(100*M + N) = O(M+N)
"""
def maxProfit(difficulty, profit, worker):
    A = [0] * 101
    for i, diff in enumerate(difficulty):
        for j in range(1, diff+1):
            A[j] = max(A[j], profit[i])

    res = 0
    for skill in worker:
        res += A[skill]
    return res

# 31. L838: https://leetcode.com/problems/push-dominoes/
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        we have 4 cases:
        L...L -> LLLLL
        L...R -> L...R
        R...R -> RRRR
        R...L -> RR.LL or RRRLLL
        
        idea:
        1. Add fake head and tail char that is dominoes = "L" + dominoes + "R"
        2. Use two pointers l and r, matches the 4 cases above, then update final states to result.
        
        Time: O(n)
        Space: O(n)
        """
        dominoes = "L" + dominoes + "R"
        l = 0
        r = 1
        res = ""
        n = len(dominoes)
        while r < n:
            if dominoes[r] != ".":
                if l > 0:
                    res += dominoes[l]
                size = r - l - 1
                if dominoes[l] == dominoes[r] == "L":
                    res += "L" * size
                elif dominoes[l] == dominoes[r] == "R":
                    res += "R" * size
                elif dominoes[l] == "L" and dominoes[r] == "R":
                    res += "." * size
                else:
                    # R...L -> RR.LL or RRRLLL
                    res += "R" * (size // 2) + "." * (size % 2) + "L" * (size // 2)
                l = r
            r += 1
        return res

# 32: L855: https://leetcode.cn/problems/exam-room/
"""
Time: seat() - O(logn)
      leave() - O(logn)
Space: O(n) for sortedlist and two maps.
"""
from sortedcontainers import SortedList
class ExamRoom:

    def __init__(self, n: int):
        self.leftToRight = {}
        self.rightToLeft = {}
        self.N = n

        def func(x):
            """
            排序因子:
            1. 该线段中点到端点之间的长度 倒序 (不能直接用线段长度倒序: 考虑座位是[0, 4, 9], seat=2而不是6)
            2. 1相等情况下, 按中点的index 正序 (sit in the seat with the lowest number)
            """
            left = x[0]
            right = x[1]
            distance = (right - left) // 2
            seat = left + (right - left) // 2 # same as (right + left) // 2
            
            # case1: we should seat at 0, so let distance bigger than normal cases
            if left == -1:
                distance = right
            # case2: we should seat at right - 1, so let distance bigger
            elif right == self.N: 
                distance = right - 1 - left
            # Other cases: DESC distance, ASC seat
            return (-distance, seat) 

        self.sortedList = SortedList(key=func)
        # 虚拟头尾
        self.addInterval(-1, n)
    
    def seat(self) -> int:  # O(logn)
        seat = -1
        left, right = self.sortedList.pop(0)
        if left == -1:
            seat = 0
        elif right == self.N:
            seat = self.N - 1
        else:
            seat = left + (right - left) // 2
        self.removeInterval(left, right)
        self.addInterval(left, seat)
        self.addInterval(seat, right)
        return seat

    def leave(self, p: int) -> None: # O(logn)
        left = self.rightToLeft[p]
        right = self.leftToRight[p]
        self.removeInterval(p, right)
        self.removeInterval(left, p)
        self.addInterval(left, right)

    def addInterval(self, left, right):  # O(logn)
        self.sortedList.add([left, right])
        self.leftToRight[left] = right
        self.rightToLeft[right] = left
    
    def removeInterval(self, left, right): # O(logn)
        self.sortedList.discard([left, right])
        self.leftToRight.pop(left)
        self.rightToLeft.pop(right)
        
        

        


# 33: L875: https://leetcode.cn/problems/koko-eating-bananas/
# Binary search
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        while left < right:
            speed = left + (right - left) // 2
            timeNeeded = 0
            for p in piles:
                timeNeeded += math.ceil(p / speed)
            # too slow -> improve speed
            if timeNeeded > h:
                left = speed + 1
            else:
                right = speed
        return left


# 34. L1110: https://leetcode.cn/problems/delete-nodes-and-return-forest/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        use Postorder travelse
        For node A,
        if A is in to_delete:
            1. if A.left != null: result.append(A.left)
               if A.right != null: result.append(A.right)
               if A in res: res.remove(res)
            2. delete A: return null
        """
        to_delete = set(to_delete)
        res = [root]
        self.postOrderDel(root, to_delete, res)
        return res
    
    def postOrderDel(self, root, to_delete, res) -> TreeNode:
        if not root:
            return None
        root.left = self.postOrderDel(root.left, to_delete, res)
        root.right = self.postOrderDel(root.right, to_delete, res)
        if root.val in to_delete:
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            if root in res:
                res.remove(root)
            return None
        return root


# 35. L1143
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp[i][j]: the LCS of t1[0...i] and t2[0...j]
        the result is dp[-1][-1]
        func: 
            if t1[i] == t2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        note: we can let dp[i][j] means the LCS of t1[0:i-1] and t2[0:j-1]
              which makes dp[0][j] = 0 and dp[j][0] = 0
              since t1[0:0] and t2[0:0] are empty string
              This will make initiation part be simple
              the result is dp[len(t1)][len(t2)]
        """
        # 1. init
        dp = []
        m = len(text1)
        n = len(text2)
        for _ in range(m+1):
            dp.append((n+1) * [0])
        # if text1[0] == text2[0]:
        #     dp[0][0] = 1
        # for i in range(1, m):
        #     if text1[i] == text2[0]:
        #         dp[i][0] = 1
        #     else:
        #         dp[i][0] = dp[i-1][0]
        # for j in range(1, n):
        #     if text1[0] == text2[j]:
        #         dp[0][j] = 1
        #     else:
        #         dp[0][j] = dp[0][j-1]
        # 2.
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]

# 36. L1235
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        dp[i] means the max profix within time i
        dp[i][0] = time, dp[i][1] = profit
        trans func:
        dp[i] = max(dp[i-j][1] + dp[i][1], dp[i-1]), j is the rightmost end time less than i
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]] # [end time, profit]
        for s, e, p in jobs:
            prev_idx = bisect.bisect(dp, s, key=lambda x:x[0]) - 1
            if dp[prev_idx][1] + p > dp[-1][1]:
                dp.append([e, dp[prev_idx][1] + p]) 
        
        return dp[-1][1]

# 37. L1268: https://leetcode.cn/problems/search-suggestions-system/
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.prefixs = []
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #1. build trie
        root = Trie()
        products.sort()
        for word in products:
            cur = root
            for ch in word:
                cur = cur.children[ch]
                cur.prefixs.append(word)

        #2. traverse Trie using searchWord
        res = []
        cur = root
        i = 0
        while i < len(searchWord):
            if searchWord[i] not in cur.children:
                break
            cur = cur.children[searchWord[i]]
            res.append(cur.prefixs[:3])
            i += 1
        while i < len(searchWord):
            res.append([])
            i += 1
        return res

# 38. L1779: https://leetcode.cn/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = float('inf')
        minDis = float('inf')
        for i, (a, b) in enumerate(points):
            if a != x and b != y:
                continue
            dis = self.getDistance(x, y, a, b)
            if minDis >= dis:
                if minDis == dis:
                    res = min(res, i)
                else:
                    minDis = dis
                    res = i
        return res if res != float('inf') else -1

        
    def getDistance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

# 39. L1905: https://leetcode.cn/problems/count-sub-islands/
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        idea: for every land in grid2,
                if the land not in grid1:
                    flood the whole island
                else: do nothing.
            Then, count the number of islands in grid2
        """
        m = len(grid2)
        n = len(grid2[0])
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    self.dfs(grid2, i, j)
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    cnt += 1
                    self.dfs(grid2, i, j)
        return cnt

    
    def dfs(self, grid2, i, j) -> None:
        m = len(grid2)
        n = len(grid2[0])
        if i < 0 or i > m - 1 or j < 0 or j > n - 1:
            return
        if grid2[i][j] == 0:
            return
        
        # flood
        grid2[i][j] = 0
        for nexti, nextj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            self.dfs(grid2, nexti, nextj)

# 40. L2065: https://leetcode.cn/problems/maximum-path-quality-of-a-graph/
class Solution:
    def __init__(self):
        self.res = 0

    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        """
        Since There are at most four edges connected to each node 
        and 10 <= timej, maxTime <= 100 that means len(path) <= 10.
        if we iterate every path, the time complexity is O(4 ** 10)
        so we could use dfs + backtracking
        """
        # build graph
        graph = dict()
        n = len(edges)
        for src, dst, time in edges:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append((dst, values[dst], time))
            graph[dst].append((src, values[src], time))
        # print(graph)
        visited = set()
        visited.add(0)
        self.backtracking(graph, visited, 0, values[0], 0, maxTime)
        return self.res
            


    def backtracking(self, graph, visited, node, quality, timeUsed, maxTime) -> None:
        if node == 0:
            self.res = max(self.res, quality)
        if node not in graph:
            return
        for neighbor,val,cost in graph[node]:
            if timeUsed + cost <= maxTime:
                if neighbor not in visited:
                    visited.add(neighbor)
                    self.backtracking(graph, visited, neighbor, quality + val, timeUsed + cost, maxTime)
                    visited.remove(neighbor)
                else:
                    self.backtracking(graph, visited, neighbor, quality, timeUsed+cost, maxTime)

# 41. 
"""
Given a list of cities' name -- c: ['C1', 'C2', 'C3'], 
the coordinates lists of the cites -- x: [1, 2, 3], y: [3, 2, 3], 
target city list -- q: ['C2', 'C3']
Find the city that shares coordinates (x or y) with the city in the target city list. If not found, return 'None'
If there are more than one city sharing coordinates, then return the one which is the closest to the target city. 
Use Manhattan Distance for distance calculating(abs(x1 - x2) + abs(y1 - y2)).
If the distances of the cities are the same, then sort the name in lexicographical order, and return the smaller one.
Example:
c: ['C1', 'C2', 'C3']
x: [1, 2, 3]
y: [3, 2, 3]
q: ['C2', 'C3']
return: ['None', 'C1']
follow up 问如何优化。
"""
"""
idea:
1. use hashmap, xMap and yMap, key is coordinate(x or y), 
    value is a SortedList of tuple(distance,city name) which sorted by distance and name. - O(ClogK)
    K is the longest lenth of citys with same coordinate.
2. for each target city, get the closest city from xMap and yMap using binarySearch,
    - get sortedList from xMap(yMap) = xMap.get(x) - O(1), 
      then do binarySearch - O(logK)
Time: O(ClogK + QlogK), Q is the len(q)
Space: the size of hashmap = O(C)
"""
from sortedcontainers import SortedList
def getClosestCity(cities: list[str], X: list[int], Y:list[int], target: list[str]) -> list[str]:
    #1. create hmaps
    cityToPos = dict()
    xmap = dict()
    ymap = dict()
    n = len(cities)
    for i in range(n):
        if X[i] not in xmap:
            xmap[X[i]] = SortedList()
        if Y[i] not in ymap:
            ymap[Y[i]] = SortedList()
        xmap[X[i]].add((Y[i], cities[i]))
        ymap[Y[i]].add((X[i], cities[i]))
        cityToPos[cities[i]] = (X[i], Y[i])
    #2.
    res = []
    for city in target:
        x, y = cityToPos[city]
        xNeighbors = xmap.get(x)
        yNeighbors = ymap.get(y)
        if len(xNeighbors) > 1 and len(yNeighbors) > 1:
            xCity = getClosestCityInLine(xNeighbors, y)
            yCity = getClosestCityInLine(yNeighbors, x)
            res.append(min(xCity, yCity))
        elif len(xNeighbors) > 1:
            res.append(getClosestCityInLine(xNeighbors, y))
        elif len(yNeighbors) > 1:
            res.append(getClosestCityInLine(yNeighbors, x))
        else:
            res.append("None")
    return res

def getClosestCityInLine(neighbors, value) -> str:
            city = ""
            index = bisect.bisect_left(neighbors, value, key=lambda v: v[0])
            if index == len(neighbors) - 1:
                city = neighbors[index - 1][1]
            elif index == 0:
                city = neighbors[index+1][1]
            else:
                if abs(y - neighbors[index+1][0]) > abs(value - neighbors[index-1][0]):
                    city = neighbors[index-1][1]
                elif abs(y - neighbors[index+1][0]) < abs(value - neighbors[index-1][0]):
                    city = neighbors[index+1][1]
                else:
                    city = min(neighbors[index+1][1], neighbors[index-1][1])
            return city


# 42.
"""
给一个unsorted 的一串数字，数字代表的是每个糖果的价格，现在有一个优惠活动叫“买二送一”，
问需要花最小的钱把所有的糖果都买下来。我类推了几个test cases，
跟他说了我的思路，先从大到小排序数组，
然后遍历数组实现“take 2 skip 1”这样就能是先用最少的钱买下所有糖果。
"""
# todo

# 43. 给List<食物价格>和List<卡路里>和一个double预算， 求预算内最大卡路里
def _01_knapsack()
# dp[j] means: within j budget, the max calorie we can gain.
    price = [1,3,4] # price
    calorie = [15, 20, 30] # calorie
    budget = 4 # budget

    dp = [0] * (budget + 1)
    for i in range(len(price)):
        for j in range(budget, price[i] - 1, -1):
            dp[j] = max(dp[j], dp[j-price[i]] + calorie[i])
    
    print(dp[-1])   

# 44. https://leetcode.com/discuss/interview-question/1367130/doordash-&#8205;&#8204;&#8204;&#8204;&#8204;&#8204;&#8205;&#8204;&#8204;&#8204;&#8204;&#8204;&#8205;&#8204;&#8205;&#8204;&#8205;&#8205;&#8204;phone-interview
"""
At DoorDash, menus are updated daily even hourly to keep them up-to-date. Each menu can be regarded as a tree. A menu can have many categories; each category can have many menu_items; each menu_item can have many item_extras; An item_extra can have many item_extra_options…

class Node {
        String key;
        int value;
        boolean active;
        List<Node> children;
 }
We will compare the new menu sent from the merchant with our existing menu. 
Each item can be considered as a node in the tree. 
The definition of a node is defined above. 
Either value change or the active status change means the node has been changed. 
There are times when the new menu tree structure is different from existing trees, 
which means some nodes are set to null. 
In this case, we only do soft delete for any nodes in the menu. 
If that node or its sub-children are null, we will treat them ALL as inactive. 
There are no duplicate nodes with the same key.

Return the number of changed nodes in the tree.

        Existing tree                                        
         a(1, T)                                                
        /       \                                                          
     b(2, T)   c(3, T)                                               
    /     \           \                                                        
d(4, T) e(5, T)   f(6, T)                                               

        New tree 
        a(1, T)
            \
           c(3, F)
               \
               f(66, T)
a(1, T) a is the key, 1 is the value, T is True for active status
For example, there are a total of 5 changed nodes. Node b, Node d, Node e are automatically set to inactive. The active status of Node c and the value of Node f changed as well.

      Existing tree                                                   
        a(1, T)                                                 
      /         \                                                 
    b(2, T)   c(3, T)                                   
  /       \           \                                          
d(4, T) e(5, T)      g(7, T)                       

            New tree
            a(1, T)
          /        \                                             
   b(2, T)         c(3, T)  
   /    |    \           \    
d(4, T) e(5, T) f(6, T)    g(7, F) 
"""
class Node:
    def __init__(self, key, value, isActive):
        self.key = key
        self.value = value
        self.isActive = isActive
        self.children = []

    def equals(self, node: 'Node'):
        if node is None:
            return False

        return self.key == node.key and self.value == node.value and self.isActive == node.isActive

def get_modified_items(oldMenu, newMenu):

    if oldMenu is None and newMenu is None:
        return 0

    count = 0
    if oldMenu is None or newMenu is None or not oldMenu.equals(newMenu):
        count += 1

    child1 = get_child_nodes(oldMenu)
    child2 = get_child_nodes(newMenu)

    for k in child1.keys():
        count += get_modified_items(child1.get(k), child2.get(k))

    for k in child2.keys():
        if k not in child1:
            count += get_modified_items(None, child2.get(k))

    return count

def get_child_nodes(menu: 'Node'):
    m = {}
    if menu is None:
        return m

    for node in menu.children:
        m[node.key] = node

    return m

# 45.
"""
给了一条题目是给了一系列Pick up和delivery的item，然后计算Dasher需要拿多少钱佣金 比如
19:00,Order A, PickUp,
19:05, Order B, PickUp
19:30, Order B, Delivered
19:40, Order A, Deilvered
一分钟的佣金是 30美分，那么这个Dasher 应该的佣金是
（19:05 - 19:00） * 30 + (19:30-19:05) * 2 (因为同时有2单) * 30 + (19:40 - 19:30) * 30 = 150+1500+300 = 1950美分

idea: build a hashmap: key is orderID, value is a tuple(pickTime, endTime)
for each order, caculate time_cost * 30.
"""

# 46
"""
https://leetcode.com/discuss/interview-question/1302606/DoorDash-onsite-interview-(new-question!)
Given a sequence of timestamps & actions of a dasher's activity within a day, 
we would like to know the active time of the dasher. 
Idle time is defined as the dasher has NO delivery at hand. 
(That means all items have been dropped off at this moment and the dasher is just waiting for another pickup) 
Active time equals total time minus idle time. Below is an example. 
Dropoff can only happen after pickup. 12:00am means midnight and 12:00pm means noon. 
All the time is within a day.

idea: can use a stack, 
when dropoff, pick_time = stack.pop(), 
            if stack.empty(), active_time += getDuration(droptime, picktime)
"""

# 47.
"""
还有一道是新题。大概意思是有一个数组，可以set（所有元素变成1）， unset（所有元素变成0），flip（所有1变成0,0变成1），
问怎么用O（1）来实现这个几个操作。
基本解题思路是，我们不可以用数组来记录真是的数值，因为这样子子flip就是O（N）。
我们用一个全局变量来记录flip的奇偶性，然后数组就记录真实值和flip的区别，
the real value at index i = （flip_count + value at index i ）% 2
"""

# 48.
"""
给一个数组，[2,5,4,9,1] 找到每一次最小的peak，就是比左右都大的数，然后输出
比如上例，输出就是5, 9, 4, 2, 1
一个数组，按大小打印元素，但元素要符合条件a[k-1]<a[k]>a[k+1]，符合这种条件的按大小打印a[k].

idea: monotonic stack, from top to bot, larger -> small
"""

# 49.Encode Hours
class StoreTime():
    def __init__(self):
        self.day = 0
        self.min = 0
    def add_minutes(self, extra_mins):
        self.min = (self.min // extra_mins) * extra_mins
        self.min += extra_mins
        if self.min >= 1440:
            self.min = self.min % 1440
            self.day += 1
            if self.day > 7 :
                self.day = self.day % 7

    def equals(self, time) -> bool:
        return self.day == time.day and self.min == time.min

    def to_format(self):
        # return "{} {}:{}".format(self.day, str(self.min//60).zfill(2), str(self.min%60).zfill(2))
        return f"{self.day}{str(self.min//60).zfill(2)}{str(self.min%60).zfill(2)}"
def get_storetime_token(s):
    dic = {
      'mon': 1,
      'tue': 2,
      'wed': 3,
      'thu': 4,
      'fri': 5,
      'sat': 6,
      'sun': 7
      }
    s = s.split(' ') 
    dt, hr, tp = s[0], s[1], s[2]
    day = dic[dt]
    extra_hour = int(12 if tp == 'pm' else 0) # 'pm'->12 , 'am'=>0
    hour = int(hr.split(':')[0])
    mins = int(hr.split(':')[1])
    st = StoreTime()
    st.day = day
    st.min = (hour+extra_hour) * 60 + mins
    return st
def conver_tokens(start, end):
    st1 = get_storetime_token(start)
    st2 = get_storetime_token(end)
    res = []
    # while st1.day * 24 * 60 + st1.min <= st2.day * 24 * 60 + st2.min:
    while not st1.equals(st2):
        st1.add_minutes(5)
        res.append(st1.to_format())
    return res
# print(conver_tokens('sun 11:55 pm', 'mon 00:05 am'))
