"""
    LC 1615 Maximal Network Rank
"""
from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """

        road - edge
        city - vertex

        Network rank of two cities - number of directly connected roads

        u   []

        v   []

        If v in u,

        adjancency list (count the edge just once)
        length of the edges list

        Pairs of cities

        Test cases

            n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]

            count_edges = [0,0,0,0]
            graph                   count_edges
                 0   [1,3]              2
                 1   [0,2,3]            3
                 3.  [0]                1
                 2.  [1]                1
           0,1           5 - 1 = 4
           0,2
           0,3

           1 2
           1 3

           2 3


           0 1 2 3

        T.C. - O(N**2)
        S.C. - O(N + M)

        How can we get to linear Time complexity
        """
        count_edges = [0] * n
        graph = defaultdict(set)

        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
            count_edges[u] += 1
            count_edges[v] += 1

        max_network_rank = 0

        def network_rank(a, b):
            return count_edges[a] + count_edges[b] - (a in graph[b])

        for i in range(n - 1):
            for j in range(i + 1, n):
                max_network_rank = max(max_network_rank, network_rank(i, j))

        return max_network_rank