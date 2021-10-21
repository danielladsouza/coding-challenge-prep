"""
    LC 124. Binary Tree Maximum Path Sum
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Post order traversal
# S.C. - O(H) - H = N for skewed tree, H = log(N) balanced tree
# T.C. - O(N) - Visit every node
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        postorder = [(root, False)]
        return_values = []

        while postorder:
            node, right_subtree_processed = postorder.pop()
            if node:
                if right_subtree_processed:
                    right_path_sum = max(0, return_values.pop())
                    left_path_sum = max(0, return_values.pop())

                    # 1. largest sum with the current node as the root
                    local_sum = left_path_sum + right_path_sum + node.val
                    max_path_sum = max(max_path_sum, local_sum)
                    return_values.append(
                        max(left_path_sum, right_path_sum) + node.val)
                else:
                    postorder.append((node, True))
                    postorder.append((node.right, False))
                    postorder.append((node.left, False))
            else:
                return_values.append(0)

        return max_path_sum

    def maxPathSum_rec(self, root: Optional[TreeNode]) -> int:
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