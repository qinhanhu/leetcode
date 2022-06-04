class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        l = len(digits)
        if l < 2:
            return n
        # find index which is all '9' after
        index = l-1
        for i in range(l-2, -1, -1):
            if int(digits[i]) > int(digits[i+1]):
                digits[i] = str(int(digits[i]) - 1)
                index = i
        result = "".join(digits[:index+1]) + "9"*(l - index - 1)
        return int(result)