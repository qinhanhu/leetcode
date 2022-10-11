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