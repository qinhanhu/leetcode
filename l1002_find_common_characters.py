class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hashmap = [0] * 26
        for char in words[0]:
            hashmap[ord(char) - ord('a')] += 1
        
        for i in range(1, len(words)):
            hashmapTemp = [0] * 26
            for char in words[i]:
                hashmapTemp[ord(char) - ord('a')] += 1
            
            for ii in range(26):
                hashmap[ii] = min(hashmap[ii], hashmapTemp[ii])
        
        res = []
        for i in range(26):
            while hashmap[i] > 0:
                res.append(chr(i + ord('a')))
                hashmap[i] -= 1
        return res