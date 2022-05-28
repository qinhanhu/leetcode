class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hmap = {}
        for i, sender in enumerate(senders):
            cnt = len(messages[i].split(' '))
            if sender not in hmap:
                hmap[sender] = cnt
            else:
                hmap[sender] += cnt
        res = sorted(hmap.items(), key=lambda kv:kv[0], reverse=True)
        res = sorted(res, key=lambda kv:kv[1], reverse=True)
        # print(res)
        return str(res[0][0])