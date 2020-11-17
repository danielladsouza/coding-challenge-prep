# 9.1 epi_judge
# 
# Space Complexity - O(h) - If the tree is skewed  left or right, O(n). If the tree is balanced, 
# O(logn) / maximum depth of the function call stack
# Time Complexity - O(n)

from collections import namedtuple

# Definition for a binary tree node.
class TreeNode:
        def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

from collections import namedtuple

class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:
        Status = namedtuple('Status', ['balanced', 'height'])
        
        def height(root):
            if root == None:
                return Status(True, 0)
            balanced_left, left_height = height(root.left)
            if not balanced_left:
                return Status(False, 0)

            balanced_right, right_height = height(root.right)
            if not balanced_right:
                return Status(False, 0)

            balanced =  abs(left_height - right_height) <= 1
            return Status(balanced, max(left_height, right_height) + 1)
                                              
        result = height(root)
        return result.balanced


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if root == None:
                return (True, 0)
            balanced_left, left_height = height(root.left)
            if not balanced_left:
                return (False, 0)

            balanced_right, right_height = height(root.right)
            if not balanced_right:
                return (False, 0)

            balanced =  abs(left_height - right_height) <= 1
            return balanced, max(left_height, right_height) + 1
                                              
        result, _ = height(root)
        return result