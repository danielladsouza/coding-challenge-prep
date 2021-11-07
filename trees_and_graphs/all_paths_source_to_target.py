"""
    L.C. 797 - All Paths from Source to Target

    [[0]]
    [[0,1], [0,2]]
    [[0,2], [0,1,3]]
    result = [[0,1,3]]
    [0,2,3]

    BFS - update the paths to the destination
"""
"""L.C. 797 All Paths From Source to Target
T.C. - Since we are using an adjacency list, the T.C - O(V + E)
S.C. - O(V + E) """

from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
            [[0]]
            [[0,1], [0,2]]
            [[0,2]]]

            result = [[0,1,3]]
            [0,2,3]

            BFS - update the paths to the destination
        """
        num_nodes = len(graph)
        result = []
        bfs_queue = deque([[0]])
        while bfs_queue:
            node_list = bfs_queue.popleft()

            for n in graph[node_list[-1]]:
                if n == num_nodes - 1:
                    result.append(node_list + [n])
                else:
                    bfs_queue.append(node_list + [n])

        return result
