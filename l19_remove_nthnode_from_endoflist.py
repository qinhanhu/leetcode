# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dumHead = ListNode(-1, head)
        left = right = dumHead
        for _ in range(n):
            right = right.next
        while right.next is not None:
            right = right.next
            left  = left.next
        left.next = left.next.next
        return dumHead.next