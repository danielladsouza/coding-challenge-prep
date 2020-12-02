# LC 429 N-ary Tree Level Order Traversal
# Time complexity O(n)
# Space complexity O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # edge case
        if not root:
            return []
        
        #BFS approach to traverse by level and collect the node data by level
        bfs_queue = deque([root])
        level_result = []
        result = []
        
        while bfs_queue:
            count = len(bfs_queue)
            while count:
                node = bfs_queue.popleft()
                if node:
                    level_result.append(node.val)
                    for c in node.children:
                        bfs_queue.append(c)
                count -= 1
            result.append(level_result)
            level_result = []
        return result
        