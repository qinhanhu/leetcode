# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = ListNode(-1, head)
        dumHead = cur
        while cur.next and cur.next.next:
            nex = cur.next
            p = cur.next.next.next
            cur.next = nex.next
            cur.next.next = nex
            nex.next = p
            cur = cur.next.next
        return dumHead.next
