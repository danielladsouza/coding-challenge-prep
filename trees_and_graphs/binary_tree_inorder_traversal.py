# LC - 94. Binary Tree Inorder Traversal
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        def helper(root, result):
            if not root:
                return

            helper(root.left, result)
            result.append(root.val)
            helper(root.right, result)
            
        result = []
        helper(root, result)
        return result