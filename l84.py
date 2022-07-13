class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]

        heights = [0] + heights + [0]
        n = len(heights)
        monoStack = [0]
        res = 0
        for i in range(1, n):
            if heights[i] > heights[monoStack[-1]]:
                monoStack.append(i)
            elif heights[i] == heights[monoStack[-1]]:
                monoStack.pop()
                monoStack.append(i)
            else:
                while monoStack and heights[i] < heights[monoStack[-1]]:
                    mid = monoStack.pop()
                    if monoStack:
                        left = monoStack[-1]
                        right = i
                        h = heights[mid]
                        w = right - left - 1
                        res = max(res, h * w)
                monoStack.append(i)
        return res
                    