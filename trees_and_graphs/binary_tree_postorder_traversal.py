# 145. Binary Tree Postorder Traversal
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        postorder = [(root, False)]
        
        while postorder:
            node, right_subtree_processed = postorder.pop()
            
            if node:
                if right_subtree_processed:
                    result.append(node.val)
                else:
                    postorder.append((node, True))
                    postorder.append((node.right, False))
                    postorder.append((node.left, False))
        
        return result

    def postorderTraversal_2(self, root: TreeNode) -> List[int]:
        
        def helper(root, result = []):
            if not root:
                return

            helper(root.left)
            helper(root.right)
            result.append(root.val)

            return result
        
        return helper(root)
