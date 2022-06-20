class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        lastNodes = []
        words = list(set(words)) # remove duplicate
        for w in words:
            curNode = trie # root
            for char in w[::-1]:
                curNode = curNode.setdefault(char, {})

            lastNodes.append(curNode)
        
        res = 0
        # print(words, lastNodes)
        for w, l in zip(words, lastNodes):
            # if lastNode is a leaf node, w is not others' suffix.
            if l == {}:
                res += len(w) + 1
        return res
            