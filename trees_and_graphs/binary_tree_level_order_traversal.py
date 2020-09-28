# LC 102. Binary Tree Level Order Traversal
# Definition for a binary tree node.

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        bfs_queue = deque([root])
        level_result = []
        
        while bfs_queue:
            count = len(bfs_queue)
            while count:
                node = bfs_queue.popleft()
                # Check for None
                if node:
                    level_result.append(node.val)
                    
                    bfs_queue.extend([node.left, node.right])
                count -= 1
            # Check for no children .. None
            if len(level_result):
                result.append(level_result)
            
            level_result = [] 
        return result