# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:  
        def find_tilt_helper(root: TreeNode) ->(int, int): # sum, tilt
            if not root:
                return (0, 0)
            l = find_tilt_helper(root.left)
            r = find_tilt_helper(root.right)
            return (l[0]+root.val+r[0], l[1]+r[1]+abs(l[0]-r[0]))
    
        return find_tilt_helper(root)[1]

        