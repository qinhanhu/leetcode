class TextEditor:

    def __init__(self):
        self.cursor = 0
        self.text = ""

    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursor] + text + self.text[self.cursor:]
        self.cursor += len(text)
        #print(f"add:{self.text, self.cursor}")

    def deleteText(self, k: int) -> int:
        left = max(self.cursor - k, 0)
        cnt = self.cursor - left
        right = self.cursor
        if left == 0:
            self.text = self.text[right:]
        else:
            self.text = self.text[:left] + self.text[right:]
        self.cursor = left
        #print(f"del:{self.text,self.cursor}")
        return cnt
        

    def cursorLeft(self, k: int) -> str:
        left = max(self.cursor - k, 0)
        self.cursor = left
        readPoint = max(left - 10, 0)
        #print(f"cursorLeft: {self.text, self.cursor}")
        if self.cursor == 0:
            return ""
        else:
            return self.text[readPoint:self.cursor]
        
        

    def cursorRight(self, k: int) -> str:
        right = min(self.cursor + k, len(self.text))
        self.cursor = right
        readPoint = max(right - 10, 0)
        #print(f"cursorRight: {self.text, self.cursor}")
        if self.cursor == 0:
            return ""
        else:
            return self.text[readPoint:self.cursor]
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)