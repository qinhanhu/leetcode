class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # magazMap = dict()
        magazMap = [0] * 26
        for char in magazine:
            magazMap[ord(char) - ord('a')] += 1
        
        for char in ransomNote:
            magazMap[ord(char) - ord('a')] -= 1
            if magazMap[ord(char) - ord('a')] < 0:
                return False
        return True