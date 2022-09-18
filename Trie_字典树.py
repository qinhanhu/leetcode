# Trie - 字典树
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.words = []