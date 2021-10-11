"""
    L.C. 124. Binary Tree Maximum Path Sum

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def helper(node: TreeNode):
            # The nonlocal keyword is used to work with variables inside nested functions,
            # where the variable should not belong to the inner function.

            nonlocal max_path_sum

            if node == None:
                return 0

            left_path = max(0, helper(node.left))
            right_path = max(0, helper(node.right))

            # 1. largest sum with the current node as the root
            local_sum = left_path + right_path + node.val
            max_path_sum = max(max_path_sum, local_sum)

            # 2. Return to my ancestor the longest sum along the path passing through me
            return max(left_path, right_path) + node.val

        helper(root)
        return max_path_sum
