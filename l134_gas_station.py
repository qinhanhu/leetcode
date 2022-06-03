class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum = 0
        totalSum = 0
        result = 0
        for i in range(len(gas)):
            dif = gas[i] - cost[i]
            curSum += dif
            if curSum < 0:
                result = i + 1
                curSum = 0
            totalSum += dif
        if totalSum < 0:
            return -1
        return result