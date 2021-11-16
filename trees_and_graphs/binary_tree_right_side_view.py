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

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        """
            BFS - deque - FIFO
        """
        if not root:
            return []

        bfs_queue = deque([root])

        def level_order_traversal(node):
            while (bfs_queue):
                count = len(bfs_queue)
                current_node = None
                # Get the last value at the current level
                last_value = float('-inf')
                while count:
                    current_node = bfs_queue.popleft()
                    last_value = current_node.val
                    if current_node.left:
                        bfs_queue.append(current_node.left)
                    if current_node.right:
                        bfs_queue.append(current_node.right)
                    count -= 1
                result.append(last_value)

        level_order_traversal(root)

        return result