class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
            if cur is None:
                return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        n = Node(val, self.head.next)
        if n.next is None:
            self.tail = n
        self.head.next = n
        

    def addAtTail(self, val: int) -> None:
        n = Node(val)
        self.tail.next = n
        self.tail = n

    def addAtIndex(self, index: int, val: int) -> None:
        n = Node(val)
        cur = self.head
        # move cur to the pre node of index
        for _ in range(index):
            cur = cur.next
            if cur is None:
                return
        nex = cur.next
        cur.next = n
        n.next = nex
        if n.next is None:
            self.tail = n
        
    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        # move cur to the pre node of index
        for _ in range(index):
            cur = cur.next
            # if the delete node or its prefix node is None
            if cur is None or cur.next is None:
                return
        n = cur.next
        cur.next = n.next
        n.next = None
        if cur.next is None:
            self.tail = cur



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)