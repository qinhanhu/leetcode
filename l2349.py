from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.indexes = {}
        self.numbers = {}
        

    def change(self, index: int, number: int) -> None:
        if number not in self.numbers:
            self.numbers[number] = SortedSet()
        self.numbers[number].add(index)
            
        if index not in self.indexes:
            self.indexes[index] = number
        else:
            if number != self.indexes[index]:
                oldNum = self.indexes[index]
                self.indexes[index] = number
                self.numbers[oldNum].discard(index)
        # print(self.numbers)
        

    def find(self, number: int) -> int:
        try:
            return self.numbers[number][0]
        except:
            return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)