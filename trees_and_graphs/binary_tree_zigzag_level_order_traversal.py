# Definition for a binary tree node.
from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        level_list = []
        bfs_queue = deque([root])

        flip = False
        while bfs_queue:
                count = len(bfs_queue)  # count of nodes from the last level.
                while count:
                    node = bfs_queue.popleft()
                    if node:
                        level_list.append(node.val)
                        bfs_queue.extend([node.left, node.right])
                    count -= 1
                
                if len(level_list):
                    if flip:
                        level_list.reverse()	
                        
                    result.append(level_list)
                    level_list = []

                flip = not flip
        return result