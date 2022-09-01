from sortedcontainers import SortedList
class ExamRoom:

    def __init__(self, n: int):
        self.leftToRight = {}
        self.rightToLeft = {}
        self.N = n

        def func(x):
            """
            排序因子:
            1. 该线段中点到端点之间的长度 倒序 (不能直接用线段长度倒序: 考虑座位是[0, 4, 9], seat=2而不是6)
            2. 1相等情况下, 按中点的index 正序 (sit in the seat with the lowest number)
            注意如果线段左右为-1 or self.N 虚拟头尾, 计算线段长度要-1
            """
            if x[0] == -1:
                return (-x[1], x[0] + (x[1] - x[0]) // 2)
            if x[1] == self.N:
                return (-(self.N - 1 - x[0]), x[0] + (x[1] - x[0]) // 2)
            return (-((x[1] - x[0]) // 2), x[0] + (x[1] - x[0]) // 2)

        self.sortedList = SortedList(key=func)
        # 虚拟头尾
        self.addInterval(-1, n)
    
    def seat(self) -> int:
        seat = -1
        left, right = self.sortedList.pop(0)
        if left == -1:
            seat = 0
        elif right == self.N:
            seat = self.N - 1
        else:
            seat = left + (right - left) // 2
        self.removeInterval(left, right)
        self.addInterval(left, seat)
        self.addInterval(seat, right)
        return seat

    def leave(self, p: int) -> None:
        left = self.rightToLeft[p]
        right = self.leftToRight[p]
        self.removeInterval(p, right)
        self.removeInterval(left, p)
        self.addInterval(left, right)

    def addInterval(self, left, right):
        self.sortedList.add([left, right])
        self.leftToRight[left] = right
        self.rightToLeft[right] = left
    
    def removeInterval(self, left, right):
        self.sortedList.discard([left, right])
        self.leftToRight.pop(left)
        self.rightToLeft.pop(right)






# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)