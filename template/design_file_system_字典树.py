# 26. LC1166: https://leetcode.com/problems/design-file-system/
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.value = 0
        
class FileSystem:

    def __init__(self):
        self.root = Trie()

    def createPath(self, path: str, value: int) -> bool:
        if len(path) <= 1:
            return False
        cur = self.root
        dictionarys = path.split("/")[1:]
        for i, dicName in enumerate(dictionarys):
            # parent dic not exists
            if i != len(dictionarys) - 1 and dicName not in cur.children:
                return False       
            cur = cur.children[dicName]
            if i == len(dictionarys) - 1:
                # already exists
                if cur.value != 0:
                    return False
                cur.value = value
        return True
        

    def get(self, path: str) -> int:
        cur = self.root
        dictionarys = path.split("/")[1:]
        for i, dicName in enumerate(dictionarys):  
            if dicName not in cur.children:
                return -1
            cur = cur.children[dicName]
        return cur.value
            
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# 27. LC588: https://leetcode.com/problems/design-in-memory-file-system/
class Trie:
    def __init__(self, name=""):
        self.children = collections.defaultdict(Trie)
        self.content = ""
        self.name = name
        
class FileSystem:

    def __init__(self):
        self.root = Trie()
        
    def ls(self, path: str) -> List[str]:
        cur = self.root
        if len(path) > 1: # not "/"
            path = path.split("/")[1:]
            for i, dicName in enumerate(path):
                if dicName not in cur.children:
                    return []
                cur = cur.children[dicName]
        res = []
        # directory path
        if not cur.content:
            for name in cur.children.keys():
                res.append(name)
            res.sort()
        else:
            # file path
            if cur.name:
                res.append(cur.name)
        return res

    def mkdir(self, path: str) -> None:
        cur = self.root
        path = path.split("/")[1:]
        for dicName in path:
            cur = cur.children[dicName]
            cur.name = dicName

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")[1:]
        cur = self.root
        for dicName in path:
            cur = cur.children[dicName]
            cur.name = dicName
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split("/")[1:]
        cur = self.root
        for dicName in path:
            if dicName not in cur.children:
                return ""
            cur = cur.children[dicName]
        return cur.content
        
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)