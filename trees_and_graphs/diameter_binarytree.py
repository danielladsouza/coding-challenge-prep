# LC 543 - Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_path = float('-inf')

        def helper(node: TreeNode):
            # The nonlocal keyword is used to work with variables inside nested functions,
            # where the variable should not belong to the inner function.

            nonlocal longest_path

            if node == None:
                return 0

            left_path = helper(node.left)
            right_path = helper(node.right)

            # 1. Longest path with the current node as the root
            local_path = left_path + right_path
            longest_path = max(longest_path, local_path)

            # 2. Return to my ancestor the longest path passing through me
            return max(left_path, right_path) + 1

        helper(root)
        return longest_path