# L.C. 687. Longest Univalue Path - https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_path = 0
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def helper(root):
            if root is None:
                return (float('-inf'), 0)
            left_status = helper(root.left)
            right_status = helper(root.right)
            
            my_path = 0
            subtree_path = 0
            
            if left_status[0] == root.val and right_status[0] == root.val:
                subtree_path = left_status[1] + 1 + right_status[1] + 1
                my_path = max(left_status[1], right_status[1]) + 1
            elif left_status[0] == root.val:
                subtree_path = left_status[1] + 1
                my_path = subtree_path
            elif right_status[0] == root.val:
                subtree_path = right_status[1] + 1
                my_path = subtree_path
                
            self.max_path = max(self.max_path, subtree_path)    
            return (root.val, my_path)
        
        helper(root)
        return self.max_path
