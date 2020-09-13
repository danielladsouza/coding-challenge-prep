"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.max_depth = 0
        
    def maxDepth(self, root: 'Node') -> int:
        def preorder_traversal_helper(root: "Node", count: int):
            if root == None:
                return
            
            # Visting my root node
            count += 1
            # Make longest path decisions when I reach a leaf node.. it does not have any children
            if len(root.children) == 0:
                if count > self.max_depth:
                    self.max_depth = count
                    return
                
            for n in root.children:
                preorder_traversal_helper(n, count)
                
        preorder_traversal_helper(root, 0)
        return self.max_depth
    