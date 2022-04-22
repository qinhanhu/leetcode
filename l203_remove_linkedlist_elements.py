# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = ListNode(-1)
        cur.next = head
        head = cur
        while cur.next is not None:
            nex = cur.next
            if nex.val == val:
                cur.next = nex.next
                nex.next = None
            else:
                cur = cur.next
        return head.next