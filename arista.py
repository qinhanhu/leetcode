# 1. L285: https://leetcode.com/problems/inorder-successor-in-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        res = None
        cur = root
        while cur:
            if p.val >= cur.val:
                cur = cur.right
            else:
                res = cur
                cur = cur.left
        return res


# 2. L165: https://leetcode.com/problems/compare-version-numbers/                        
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        j = 0
        m = len(version1)
        n = len(version2)
        while i < m or j < n:
            val1 = 0
            val2 = 0
            while i < m and version1[i] != ".":
                val1 += val1 * 10 + int(version1[i])
                i += 1
            # skip "."    
            i += 1
            
            while j < n and version2[j] != ".":
                val2 += val2 * 10 + int(version2[j])
                j += 1
            j += 1
            
            if val1 != val2:
                return 1 if val1 > val2 else -1
        return 0
            


# 3. L1852: https://leetcode.com/problems/distinct-numbers-in-each-subarray/
class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = {}
        cnt = 0
        res = []
        left = 0
        right = 0
        while right < n:
            if nums[right] not in counter:
                counter[nums[right]] = 0
            counter[nums[right]] += 1
            if right - left + 1 == k:
                res.append(len(counter))
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            right += 1
        return res

# 4. L510: https://leetcode.com/problems/inorder-successor-in-bst-ii/
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        """
        if node.right:
            return leftmost(node.right)
        else:
            traverse to his parent until meet a node who has larger value
        
        """
        
        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur
        cur = node.parent
        while cur:
            if cur.val > node.val:
                return cur
            else:
                cur = cur.parent
        return cur

# 5. L545: https://leetcode.com/problems/boundary-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.leftBoundary = []
        self.leaves = []
        self.rightBoundary = []
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        flag = 0: root
        flag = 1: left boundary
        flag = 2: right boundary
        flag = 3: others
        """
        
        self.preorder(root, 0)
        return [root.val] + self.leftBoundary + self.leaves + self.rightBoundary[::-1]
    
    def getLeftChildFlag(self, node, flag) -> int:
        if flag == 0 or flag == 1:
            return 1
        elif flag == 2 and node.right is None:
            return 2
        return 3
        
    def getRightChildFlag(self, node, flag) -> int:
        if flag == 0 or flag == 2:
            return 2
        elif flag == 1 and node.left is None:
            return 1
        return 3
    
    def preorder(self, root, flag):
        if not root:
            return 
        if flag == 1:
            self.leftBoundary.append(root.val)
        elif flag == 2:
            self.rightBoundary.append(root.val)
        # the root is not a leaf
        elif not root.left and not root.right and flag != 0:
            self.leaves.append(root.val)
            
        self.preorder(root.left, self.getLeftChildFlag(root, flag))
        self.preorder(root.right, self.getRightChildFlag(root, flag))

# 6. L268: https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return sum([i for i in range(n+1)]) - sum(nums)


# 7. L430: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def __init__(self):
        self.tail = None
        
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        while cur:
            if cur.next is None:
                self.tail = cur
            next = cur.next
            if cur.child:
                childHead = self.flatten(cur.child)
                cur.child = None
                cur.next = childHead
                childHead.prev = cur
                if self.tail and next:
                    self.tail.next = next
                    next.prev = self.tail
            cur = next

        return head

# 8. L1071: https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            n = len(str1)
            m = len(str2)
            return str1[:self.gcd(n, m)]
        return ""
        
    
    def gcd(self, a:int, b:int) -> int:
        bigger = max(a, b)
        smaller = min(a, b)
        if bigger % smaller == 0:
            return smaller
        return gcd(bigger % smaller, smaller)

# 9. L83: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        fakehead = ListNode(-101, head)
        prev = fakehead
        cur = head
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return fakehead.next

# 10. L101: https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, leftNode, rightNode):
        if not leftNode and not rightNode:
            return True
        elif not leftNode or not rightNode:
            return False
        
        if leftNode.val != rightNode.val:
            return False
        
        return self.compare(leftNode.left, rightNode.right) and self.compare(leftNode.right, rightNode.left)


# 11. L56: https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for i in range(1, n):
            if intervals[i][0] <= end and intervals[i][1] > end:
                end = intervals[i][1]
            elif intervals[i][0] > end:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start, end])
        return res

# 12. L997: https://leetcode.cn/problems/find-the-town-judge/
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        1. caculate indegree and outdegree for every node
        2. find if there exists a node having 0 outdegree and n - 1 indegree
        """
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)
        for src, dst in trust:
            outdegree[src] += 1
            indegree[dst] += 1
        for i in range(1, n + 1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1


# 13. L2182: https://leetcode.cn/problems/construct-string-with-repeat-limit/
import heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = dict()
        for ch in s:
            if ch not in counter:
                counter[ch] = 0
            counter[ch] += 1
        maxheap = []
        for ch, cnt in counter.items():
            heapq.heappush(maxheap, (-ord(ch), cnt))
        
        res = ""
        while maxheap:
            largest = heapq.heappop(maxheap)
            if repeatLimit >= largest[1]:
                res += chr(-largest[0]) * largest[1]
            else:
                res += repeatLimit * chr(-largest[0])
                if maxheap:
                    secondLarge = heapq.heappop(maxheap)
                    res += chr(-secondLarge[0])
                    if secondLarge[1] - 1 > 0:
                        heapq.heappush(maxheap, (secondLarge[0], secondLarge[1] - 1))
                    heapq.heappush(maxheap, (largest[0], largest[1] - repeatLimit))
        return res

# 14 L93: https://leetcode.com/problems/restore-ip-addresses/
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def backtracking(s, start:int):
            if len(self.path) > 4:
                return
            if start == len(s) and len(self.path) == 4:
                self.res.append(".".join(self.path))
                return
            
            for i in range(start, len(s)):
                if i - start + 1 > 3:
                    return
                if self.isLeadingZero(s[start:i+1]):
                    return
                if int(s[start:i+1]) > 255:
                    return
                self.path.append(s[start:i+1])
                backtracking(s, i+1)
                self.path.pop()
        
        backtracking(s, 0)
        return self.res
        

    def isLeadingZero(self, s:str):
        if s == "0":
            return False
        elif s[0] == "0":
            return True
        return False