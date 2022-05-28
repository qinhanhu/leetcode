class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        hmap = {}
        for r in roads:
            if r[0] not in hmap:
                hmap[r[0]] = []
            if r[1] not in hmap:
                hmap[r[1]] = []
            
            hmap[r[0]].append(r[1])
            hmap[r[1]].append(r[0])
        h = sorted(hmap.items(), key=lambda x:len(x[1]), reverse=True)
        hmap_v = {}
        val = n
        for i in h:
            hmap_v[i[0]] = n
            n -= 1
        res = 0
        for r in roads:
            res += hmap_v[r[0]] + hmap_v[r[1]]
        return res