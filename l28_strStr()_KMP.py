class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(pat: str) -> list:
            # 1. init
            j = 0
            next = [0] * len(pat)
            for i in range(1, len(pat)):
                # 2. prefix != suffix
                while j > 0 and pat[i] != pat[j]:
                    j = next[j-1]
                # 3. prefix == suffix
                if pat[i] == pat[j]:
                    j += 1
                next[i] = j
            return next
        def KMP(txt: str, pat: str) -> int:
            if len(pat) == 0:
                return 0
            next = getNext(pat)
            j = 0
            for i in range(len(txt)):
                while j > 0 and txt[i] != pat[j]:
                    j = next[j-1]
                if txt[i] == pat[j]:
                    j += 1
                if j == len(pat):
                    return i - len(pat) + 1
            return -1
        
        return KMP(haystack, needle)