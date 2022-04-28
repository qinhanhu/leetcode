from collections import deque
class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return
        cnt = len(self.que) - 1
        for _ in range(cnt):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        if self.empty():
            return
        t = self.pop()
        self.push(t)
        return t

    def empty(self) -> bool:
        return len(self.que) == 0