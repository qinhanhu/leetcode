
# binary search - 二分
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix = ""
        res = []
        for ch in searchWord:
            prefix += ch
            left = self.lowerBound(products, 0, len(products), prefix)
            match = []
            for i in range(left, left + 3):
                if i <= len(products) - 1:
                    if products[i][:len(prefix)] == prefix:
                        match.append(products[i])
            
            res.append(match)
        return res

    
    def lowerBound(self, array, left, right, value):
        while left < right:
            mid = left + (right - left) // 2
            if array[mid] < value:
                left = mid + 1
            else:
                right = mid
        return left


# Trie - 字典树
import collections
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.words = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = Trie()
        for p in products:
            cur = root
            for ch in p:
                cur = cur.children[ch]
                if len(cur.words) < 3:
                    cur.words.append(p)
        cur = root
        res = []
        for ch in searchWord:
            cur = cur.children[ch]
            res.append(cur.words)
        return res
