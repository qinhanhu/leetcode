class Solution:
    def __init__(self):
        self.path = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def backtracking(tickets, airport: str, used:List[bool]):
            if len(self.path) == len(tickets):
                self.path.append(airport)
                return True
            
            for i in range(len(tickets)):
                if used[i] is True:
                    continue
                if tickets[i][0] == airport:
                    self.path.append(airport)
                    used[i] = True
                    dst = tickets[i][1]
                    if backtracking(tickets, dst, used):
                        return True
                    self.path.pop()
                    used[i] = False
        tickets.sort()
        used = [False] * len(tickets)
        backtracking(tickets, "JFK", used)
        return self.path


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # defaultdic(list) 是为了方便直接append
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
        '''
        tickets_dict里面的内容是这样的
         {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        '''
        path = ["JFK"]
        def backtracking(start_point):
            # 终止条件
            if len(path) == len(tickets) + 1:
                return True
            tickets_dict[start_point].sort()
            for _ in tickets_dict[start_point]:
                #必须及时删除，避免出现死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                # 只要找到一个就可以返回了
                if backtracking(end_point):
                    return True
                path.pop()
                tickets_dict[start_point].append(end_point)

        backtracking("JFK")
        return path

                


        
        