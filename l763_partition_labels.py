class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        hmap = [] 
        for _ in range(26): hmap.append([]) 
        for i in range(n):
            hmap[ord(s[i]) - ord('a')].append(i)
        # print(hmap)
        res = []
        maxRange = 0
        preReange = 0
        for i in range(n):
            maxRange = max(maxRange, hmap[ord(s[i]) - ord('a')][-1])
            if i == maxRange:
                res.append(maxRange - preReange + 1)
                preReange = maxRange + 1
        return res