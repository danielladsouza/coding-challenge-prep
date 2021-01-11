# Definition for a binary tree node.
# LC 543
# [1,2,3,4,5]
"""
    Height of a binary tree is the maximum depth of any node in that tree

    Depth of a node is the longest path from the root to that node not
    including the root
    Height of a node in a binary tree =
    The max of the height of it's left subtree and the right subtree + 1
    A successor (left/right node)  is always one edge away from it's ancestor
"""

from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        """
            Time Complexity - log(N)
            Space Complexity - Log(1)
        """

        if root is None:
            return 0
        
        def height(node: TreeNode) -> int:
            if root is None:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            diameter = left_height + right_height
            self.diameter = max(diameter, self.diameter)
            # We are ascending one level / endge
            return 1 + max(left_height, right_height)
            
        height(root)
        return self.diameter

