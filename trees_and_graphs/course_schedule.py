# LC 207. Course Schedule
from typing import List
from collections import defaultdict

class Solution1:
    # Not the best solution, because we have to check for multiple edge cases.

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
	    # Build the graph
        
        if not prerequisites:
            return True
        
        graph = defaultdict(set)
        
        #[[2,0],[1,0],[3,1],[3,2],[1,3]]

        for p in prerequisites:
            graph[p[0]].add(p[1])
	
        def has_cycle(graph, course, visited = []):
            print(course)
            if course in graph:
                if course in visited:
                    return True
                visited.append(course)
                print(visited)
            return any (has_cycle(graph, prereq) for prereq in graph[course])
        
        for source in range(numCourses + 1):
            if source in graph:
                cycle_detected = has_cycle(graph, source)
                print(source, cycle_detected)
                if (cycle_detected):
                    return False
        return True

"""
    This is a topological sort problem. We want to create an ordering of nodes such that for any edge (a, b), a will come before b in the ordering. 
    One way of visualizing a topological sort  is that if the graph is drawn in topological sort order from left to right, then all the edges should go from left 
    to right. 
    This is just the same as our prerequisite requirement, and the problem even describes the prerequisite "course A depends on course B" as the edge (A, B).
    A topological sort is impossible if there's a cycle in the graph, so ultimately what we're doing is looking for a cycle. 
    If there is a cycle then finishing the courses is impossible; otherwise it's possible.

    There are a couple of topological sort algorithms such as Kahn's algorithm, but this solution will use the DFS approach.
    The basic idea is that by doing a DFS we will reach the nodes in the back of the ordering first; 
    the "leaves" of the graph are the nodes that don't have any edges going out of them and therefore don't have any nodes that must come after them. 

    The one difference here is that we need to check for cycles, so we keep check of which nodes we have visited in our DFS. When dfs(X) is called, 
    we mark X as visiting. We then look at all the nodes that have an edge going from X to them. If that neighbor N hasn't been visited yet,
     then recursively call dfs on that neighbor. If that neighbor has been visited already but hasn't completed, then we have a cycle and can return False. 
     If all the neighbors are searched, then we are done with X and can mark it as finished.

    With this DFS algorithm, we can then run DFS() on all the nodes. If they all pass then we can return True. 

            A
           /
         B
       /  \
      D    C

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        for prereq in prerequisites:
            adjList[prereq[0]].add(prereq[1])

        import enum
        class Visit(enum.Enum):
            unvisited = 0
            visiting = 1
            finished = 2

        node_status = [ Visit.unvisited for _ in range(numCourses) ]

        class CycleException(Exception):
            pass

        def dfs(node):
            if node_status[node] == Visit.unvisited:
                node_status[node] = Visit.visiting

            for neighbor in adjList[node]:
                if node_status[neighbor] == Visit.visiting:
                    raise CycleException

                elif node_status[neighbor] == Visit.unvisited:
                    dfs(neighbor)

            node_status[node] = Visit.finished
        try:
            for course in range(numCourses):
                dfs(course)
        except CycleException:  # If cycles detected for any of the courses we fail
            return False

        return True



s = Solution1()
#result = s.canFinish(3, [[0,1],[0,2],[1,2]])

result = s.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]])
print(result)

