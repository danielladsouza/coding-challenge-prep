# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0

        def height(root):
            if root == None:
                return 0

            lheight = height(root.left)
            rheight = height(root.right)
            total_height = lheight + rheight
            self.diameter = max(self.diameter, total_height)
            
            return 1 + max(lheight, rheight)
        
        height(root)
        return self.diameter