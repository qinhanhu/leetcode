class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        n = len(asteroids)
        for i in range(1, n):
            if stack and asteroids[i] < 0:
                while stack and stack[-1] > 0 and abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                if stack and stack[-1] > 0 and abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    continue
                elif stack and stack[-1] > 0 and abs(asteroids[i]) < abs(stack[-1]):
                    continue
                else:
                    stack.append(asteroids[i])
            else:
                    stack.append(asteroids[i])
        return stack

