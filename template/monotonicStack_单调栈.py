"""
单调栈里只存下标，根据题意搞清楚栈的“方向”，从top到bot，下标对应的值是从大到小还是从小到大。
剩下就是分析清楚如下三种情况：
情况一：当前遍历的元素heights[i]小于栈顶元素heights[st.top()]的情况
情况二：当前遍历的元素heights[i]等于栈顶元素heights[st.top()]的情况
情况三：当前遍历的元素heights[i]大于栈顶元素heights[st.top()]的情况
"""
# https://leetcode.cn/problems/largest-rectangle-in-histogram/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use monotonic stack to 
        """
        1. For height i, find the left and right closest coloumns which are shorter then height[i].(MonoticStack)
        2. Caculate area = height[i] * (right - left - 1)
        i.e. heights = [2,1,5,6,2,3]
             for i = 2, height[2] = 5
             left = 1
             right = 4
             width = right - left - 1 = 2
             height = height[2] = 5
             area = width * height = 10
        """

        # From top to bot, larger to smaller. i.e. height[monoStack[i]] > height[monoStack[i+1]]
        n = len(heights)
        if n < 2:
            return heights[0] if n == 1 else 0
        heights = [0] + heights + [0]
        n = len(heights)
        monoStack = [0]
        area = 0
        for i in range(1, n):
            if heights[i] > heights[monoStack[-1]]:
                monoStack.append(i)
            elif heights[i] == heights[monoStack[-1]]:
                monoStack.append(i)
            else:
                while monoStack and heights[i] < heights[monoStack[-1]]:
                    mid = monoStack.pop()
                    left = monoStack[-1]
                    right = i
                    width = right - left - 1
                    h = heights[mid]
                    area = max(area, width * h)
                monoStack.append(i)

        # # Simplify:
        # for i in range(1, n):
        #     while monoStack and heights[i] < heights[monoStack[-1]]:
        #         mid = monoStack.pop()
        #         left = monoStack[-1]
        #         right = i
        #         width = right - left - 1
        #         h = heights[mid]
        #         area = max(area, width * h)
        #     monoStack.append(i)
        return area

        

        