# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head.next
        que = deque()
        while cur:
            que.append(cur)
            cur = cur.next
        cur = head
        while len(que) > 0:
            cur.next = que.pop()
            cur = cur.next
            if len(que) > 0:
                cur.next = que.popleft()
                cur = cur.next
        cur.next = None


            