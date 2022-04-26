class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(mutableStr: list, begin: int, end: int):
            left, right = begin, end
            while left < right:
                mutableStr[left], mutableStr[right] = mutableStr[right], mutableStr[left]
                left += 1
                right -= 1

        def deleteExtraSpace(s: str) -> list:
            mutableStr = list(s.strip())
            slow = fast = 0
            for fast in range(len(mutableStr)):
                if fast > 0 and mutableStr[fast] == ' ' and mutableStr[fast-1] == ' ':
                    continue
                else:
                    mutableStr[slow] = mutableStr[fast]
                    slow += 1
            return mutableStr[:slow]

        newS = deleteExtraSpace(s)
        reverse(newS, 0, len(newS) - 1)
        
        begin = end = 0
        for i in range(len(newS)):
            if newS[i] == ' ':
                end = i - 1
                reverse(newS, begin, end)
                begin = i + 1
            if i == len(newS) - 1:
                end = i
                reverse(newS, begin, end)
        return "".join(newS) 
        
            
                
            
            