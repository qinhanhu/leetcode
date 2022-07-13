class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0
        monoStack = [0]
        res = 0
        for i in range(1, n):
            if height[i] == height[monoStack[-1]]:
                monoStack.pop()
            else:
                while monoStack and height[i] > height[monoStack[-1]]:
                    bot = height[monoStack.pop()]
                    if monoStack:
                        h = min(height[monoStack[-1]], height[i]) - bot
                        w = i - monoStack[-1] - 1
                        res += h * w
            monoStack.append(i)
        return res