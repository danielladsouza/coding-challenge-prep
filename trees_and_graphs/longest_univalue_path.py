# L.C. 687. Longest Univalue Path - https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import namedtuple
class Solution:
    def __init__(self):
        self.max_path = 0
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        Status = namedtuple('Status', ['value', 'path'])
        def helper(root):
            if root is None:
                return Status(value=float('-inf'), path=0)

            left_status = helper(root.left)
            right_status = helper(root.right)
            
            my_path = 0
            subtree_path = 0
            
            if left_status.value == root.val and right_status.value == root.val:
                subtree_path = left_status.path + 1 + right_status.path + 1
                my_path = max(left_status.path, right_status.path) + 1
            elif left_status.value == root.val:
                my_path = subtree_path = left_status.path + 1
            elif right_status.value == root.val:
                my_path = subtree_path = right_status.path + 1
     
            self.max_path = max(self.max_path, subtree_path)    
            return Status(value=root.val, path=my_path)
        
        helper(root)
        return self.max_path
