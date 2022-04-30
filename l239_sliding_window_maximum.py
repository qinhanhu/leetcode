from collections import deque
class MonotonicQueue:
    def __init__(self):
        self.que = deque()

    def pop(self, x: int) -> int:
        if not self.isEmpty() and x == self.que[0]:
            return self.que.popleft()
        return None

    def push(self, x: int):
        while not self.isEmpty() and x > self.que[-1]:
            self.que.pop()
        self.que.append(x)
            
    def isEmpty(self) -> bool:
        return len(self.que) == 0


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        moque = MonotonicQueue()
        for i in range(k):
            moque.push(nums[i])
        res = [moque.que[0]]
        for i in range(k, len(nums)):
            # print(moque.que)
            moque.pop(nums[i-k])
            moque.push(nums[i])
            res.append(moque.que[0])
        return res