"""
Note: SortedList 直接更新排序key的值不会动态更新排序,要先del key,再add.


idea:
Trie to store relationship between prefix and sentences
i.e. sentences = ["i love", "island"]
Trie: {"root": 
            {"i": 
                {" ":
                    {"l":
                        {"o":
                            {"v":
                                {"e",
      }}}}}}}
so if node is "i", node.children = Trie{" ":{..}, "s":{..}}
                   node.prefixs = [("i love", 5), ("island", 3)]
    so if inputStr is  "i", we traverse through Trie,
    we can get top 3 hot sentences from node.prefixs
    if user finished input, i.e. inputStr = "i like#"
    we also need traverse Trie and add/update "i like" to all curNode.prefix sorted list.

"""
import collections
from sortedcontainers import SortedList
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.prefixs = SortedList(key=lambda x:(-x[1], x[0]))
        # self.prefixs = []
class AutocompleteSystem:

    def __init__(self, sentences: list[str], times: list[int]):
        self.topK = 3
        self.inputStr = ""
        self.root = Trie()
        for i,word in enumerate(sentences):  # O(N)
            cur = self.root
            for ch in word:
                cur = cur.children[ch]
                cur.prefixs.add([word, times[i]])       # O(logn)
                # cur.prefixs.append([word, times[i]])
                # cur.prefixs.sort(key=lambda x:(-x[1], x[0]))
        
    def input(self, c: str) -> list[str]:
        cur = self.root
        # finish input, update historial sentence
        if c == "#":
            for ch in self.inputStr: # O(N)
                cur = cur.children[ch]
                find = False
                for i, (prefix, time) in enumerate(cur.prefixs): # O(n)
                    if prefix == self.inputStr:
                        find = True
                        # cur.prefixs[i][1] += 1
                        # cur.prefixs.sort(key=lambda x:(-x[1], x[0]))
                        del cur.prefixs[i]
                        cur.prefixs.add([prefix, time + 1])     # O(logn)
                if not find:
                    cur.prefixs.add([self.inputStr, 1])
                    # cur.prefixs.append([self.inputStr, 1])
                    # cur.prefixs.sort(key=lambda x:(-x[1], x[0]))
            # print(cur.prefixs)
            self.inputStr = ""
            return []
        
        self.inputStr += c
        for ch in self.inputStr:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]
        # print(cur.prefixs)
        res = []
        for prefix, _ in cur.prefixs[:3]:
            res.append(prefix)
        return res
            