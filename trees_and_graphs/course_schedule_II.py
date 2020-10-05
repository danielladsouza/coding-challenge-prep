# 210. Course Schedule II

from enum import IntEnum
from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        
        # ! Build graph
        graph = defaultdict(set)
        for p in prerequisites:
            graph[p[0]].add(p[1])
            
        # Topological sort - all the courses if lined up in a sort should be pointing in the 
        # same direction
        
        class Visit(IntEnum):
            UNVISITED = 0,
            VISITING = 1,
            VISITED = 2
        
        # Initialize the visiting state of all the nodes in the graph
        visit_state = [Visit.UNVISITED for n in range(numCourses)]
        
        class CycleException(Exception):
            pass
        
        # Find all paths from a node to a leaf node (no prereqs) without cycles
        result = []
        def dfs(node):
            if visit_state[node] == Visit.UNVISITED:
                visit_state[node] = Visit.VISITING
                
            for prereqs in graph[node]:
                if visit_state[prereqs] == Visit.VISITING:
                    raise CycleException
                    
                if visit_state[prereqs] == Visit.UNVISITED:
                    dfs(prereqs)
                    
            visit_state[node] = Visit.VISITED
            result.append(node)  # the result will hold the nodes starting from the lower levels and working thier way up..

        
        for n in range(numCourses):
            try:
                # Node should appear only once in the path
                if visit_state[n] == Visit.UNVISITED:
                    dfs(n)
            except(CycleException):
                return []
        
        return result


s = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
result = s.findOrder(numCourses, prerequisites)
print(result)
