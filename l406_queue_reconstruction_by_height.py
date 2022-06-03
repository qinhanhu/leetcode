class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        if n < 2:
            return people
        people.sort(key=lambda x:(-x[0], x[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result