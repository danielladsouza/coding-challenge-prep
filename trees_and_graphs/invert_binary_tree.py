# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Post Order Traversal
        def invert_helper(root:TreeNode):
            if root == None:
                return
            
            invert_helper(root.left)
            invert_helper(root.right)
            
            root.left, root.right = root.right, root.left
            
            return root
        
        invert_helper(root)
        return root