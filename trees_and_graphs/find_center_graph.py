"""
    1791. Find Center of Star Graph
"""
from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        The key here is that the center node will appear in every edge, and all other nodes will only appear once. Simply look for an node that appears more than once in edges, and that will be the center. You don't even need to check more than 2 edges.

        O(1) time
        O(1) space
        """
# edges = [[1,2],[2,3],[4,2]]
#             X    Y
class Solution:
    """
        There are at least 3 nodes, 2 edges always present
        Hint - If the node is the center of the graph, then it will be part of every edge.
        T.C. - O(1)
        S.C. - O(1)
    """
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[1]
        if a in edges[0]:
            return a
        else:
            return b