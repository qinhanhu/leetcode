class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            sum_ = 0
            while n != 0:
                sum_ += (n % 10) * (n % 10)
                n = n // 10
            return sum_
        
        hashmap = {}
        sum_ = getSum(n)
        while sum_ != 1:
            if sum_ in hashmap:
                return False
            hashmap[sum_] = 1
            sum_ = getSum(sum_)
        return True
