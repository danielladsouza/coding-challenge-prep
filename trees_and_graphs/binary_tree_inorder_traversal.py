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

    def inorderTraversal_2(self, root: TreeNode) -> List[int]:
        result = []
        
        inorder = [(root, False)]
        
        while inorder:
            node, leftsubtree_processed = inorder.pop()
            if node:
                if leftsubtree_processed:
                    result.append(node.val)
                else:
                    inorder.append((node.right, False))
                    inorder.append((node, True))
                    inorder.append((node.left, False))
                                   
        return result