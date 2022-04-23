class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in t:
            if i not in hashmap:
                return False
            hashmap[i] -= 1
        for _, v in hashmap.items():
            if v != 0:
                return False
        return True