class MyQueue:

    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, x: int) -> None:
        self.stackIn.append(x)

    def pop(self) -> int:
        if self.empty():
            return
        if self.stackOut:
            return self.stackOut.pop()
        while self.stackIn:
            self.stackOut.append(self.stackIn.pop())
        return self.stackOut.pop()
            
    def peek(self) -> int:
        if self.empty():
            return
        if self.stackOut:
            return self.stackOut[-1]
        while self.stackIn:
            self.stackOut.append(self.stackIn.pop())
        return self.stackOut[-1]

    def empty(self) -> bool:
        return not self.stackIn and not self.stackOut



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()