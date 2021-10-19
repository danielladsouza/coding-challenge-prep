"""
    LC 1971 - Find if Path exists in graph
    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
    n <= 2 * 10 ** 5 (Max recursion depth can be exceeded with these many values of n
    Dijkstra's algorithm - shortest path from node u to node v.
    Use a better algorithm tha a brute force traversal from u to v
"""
from typing import List
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int,
                  end: int) -> bool:
    """
        BFS preferable, because we just want to know if a path exists
        We could settle with the shortest path, leading to a better time complexity
        Check the neighbors of the current node.
        Note - Use of FIFO deque for the frontier
    """
        def build_graph():
            graph = defaultdict(set)
            for u, v in edges:
                graph[u].add(v)
                graph[v].add(u)
            return graph

        graph = build_graph()
        seen = set()

        """
            edges = [[0,1],[1,2],[2,0]]
            graph 0.   1,2
                  1.   0,2
                  2.   1,0            
        """

        frontier = deque([start])  # Starting node

        while frontier:
            #FIFO queue
            u = frontier.popleft()

            if u in seen:
                continue

            if u == end:
                return True

            seen.add(u)
            for v in graph[u]:
                frontier.append(v)

        return False

    def validPath_(self, n: int, edges: List[List[int]], start: int,
                  end: int) -> bool:
        """
            DFS Time complexity O(N) if skewed, O(Log N) if balanced
            Has the overhead of recursive function calls.
            If n is very large, this will fail to run due to recursion time limit exceeded.
        """
        if n == 1:
            return True

        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Need an iterative preorder traversal

        def is_reachable_dfs(graph, curr, dest, visited=set()):
            if curr == dest:  # Found the destination node
                return True
            # reached a dead end
            elif curr in visited or curr not in graph:  # Case when the node stands on its own
                return False

            visited.add(curr)
            return any(is_reachable_dfs(graph, u, dest) for u in graph[curr])

        return is_reachable_dfs(graph, start, end)
