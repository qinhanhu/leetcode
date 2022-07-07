from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            hmap[word].append(strs[i])
            
        return list(hmap.values())