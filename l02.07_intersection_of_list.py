# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        walkerA = headA
        walkerB = headB
        cntA = cntB = 0
        while walkerA is not None:
            walkerA = walkerA.next
            cntA += 1
        while walkerB is not None:
            walkerB = walkerB.next
            cntB += 1
        diff = abs(cntA - cntB)

        walkerA = headA
        walkerB = headB
        if cntA >= cntB:
            for _ in range(diff):
                walkerA = walkerA.next
        else:
            for _ in range(diff):
                walkerB = walkerB.next
        while walkerA is not None:
            if walkerA == walkerB:
                return walkerA
            walkerA = walkerA.next
            walkerB = walkerB.next
        return None