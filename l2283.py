class Solution:
    def digitCount(self, num: str) -> bool:
        hmap = {}
        for i in range(len(num)):
            if int(num[i]) not in hmap:
                hmap[int(num[i])] = 1
            else:
                hmap[int(num[i])] += 1
        for i in range(len(num)):
            cnt = hmap.get(i)
            print(i, cnt)
            if cnt is None and int(num[i]) != 0:
                return False
            elif cnt is not None and cnt != int(num[i]):
                return False
        return True