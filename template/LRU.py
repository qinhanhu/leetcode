class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleList:
    def __init__(self):
        self.size = 0
        self.head = Node(-1, -1) # fake nodes
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def pop(self) -> 'Node':
        if self.head.next == self.tail:
            return None
        node = self.head.next
        self.remove(node)
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = DoubleList()
        self.hmap = dict()
        self.capacity = capacity
    
    # make key to be most recent (key must exist)
    def makeRecent(self, key):
        node = self.hmap[key]
        self.cache.remove(node)
        self.cache.append(node)
    
    # remove a key from cache and hmap
    def removeKey(self, key):
        node = self.hmap[key]
        self.cache.remove(node)
        del self.hmap[key]
    
    # append new (key, value) to cache and hmap
    def appendRecent(self, key, value):
        node = Node(key, value)
        self.cache.append(node)
        self.hmap[key] = node
    
    # remove least rencently used node
    def removeLeastRecent(self):
        nodeRemoved = self.cache.pop()
        del self.hmap[nodeRemoved.key]
        

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        self.makeRecent(key)
        return self.hmap[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.removeKey(key)
            self.appendRecent(key, value)
        else:
            if self.cache.size == self.capacity:
                self.removeLeastRecent()
            self.appendRecent(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)