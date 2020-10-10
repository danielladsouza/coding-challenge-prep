# 841. Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

from collections import defaultdict
from typing import List, Dict

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        
        def build_graph(rooms: List[List[int]]) -> Dict:
            graph = defaultdict(set)
            for i, r in enumerate(rooms):
                for n in r:
                    graph[i].add(n)
                    
            return graph
                     
        def helper(graph, curr, visited=set()) -> bool:
            if curr in visited:
                return False
            
            visited.add(curr)
            
            if len(visited) == N:
                return True
            
            return any(helper(graph, room) for room in graph[curr])
         
        return helper(build_graph(rooms), 0)


s = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
# rooms = [[1], [2], [3], []]
result = s.canVisitAllRooms(rooms)
print(result)