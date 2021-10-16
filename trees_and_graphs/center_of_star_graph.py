"""
    LC 1791. Find Center of Star Graph
"""
from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
            The center of the star graph is connected to every other node in the graph
            Given a graph with n nodes, the center of the star graph should be connected to the n-1 nodes.

            Parse the list of edges and store the connections from a node to other nodes in a connections map

            After forming the connections map, get a count of the connections from each node. If the count is equal to n-1 we have found the center of the star graph

            T.C - O(N)
            S.C. - O(N) + O(N) = O(N)
        """
        connections = defaultdict(set)

        # undirected graph
        for u, v in edges:
            connections[u].add(v)
            connections[v].add(u)

        # Get the total count of nodes
        n = len(connections)

        for node, nodes_connected_to in connections.items():
            if len(nodes_connected_to) == n - 1:
                return node

        return -1