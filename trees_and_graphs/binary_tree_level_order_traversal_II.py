# Definition for a binary tree node.
from collections import deque
from typing import List

class TreeNode:
        def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = deque()
        level_list = []
        bfs_queue = deque([root])

        while bfs_queue:
            count = len(bfs_queue)  # count of nodes from the last level.
            while count:
                node = bfs_queue.popleft()
                if node:
                    level_list.append(node.val)
                    bfs_queue.extend([node.left, node.right])
                count -= 1

            if len(level_list):
                # last level entries should be first in the result
                result.appendleft(level_list)
                level_list = []

        return result