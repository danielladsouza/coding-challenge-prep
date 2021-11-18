"""
    LC 199 Binary Tree Right Side View

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity - O(N)
# Space Complexity - O(N) - If all nodes were on the same level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        bfs_queue = deque([root])
        count = 0
        while bfs_queue:
            count = len(bfs_queue)
            current_node = last_node = None

            while count:
                current_node = bfs_queue.popleft()
                if current_node.left:
                    bfs_queue.append(current_node.left)
                if current_node.right:
                    bfs_queue.append(current_node.right)

                last_node = current_node
                count -= 1

            if last_node:
                result.append(last_node.val)

        return result