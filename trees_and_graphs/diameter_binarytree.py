# LC 543 - Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # S.C. - O(N) - Unbalanced
        #        O(logN)  Balanced

        # T.C. - O(N)
        # We simulate the recursive function call stack
        # process the left and right child nodes first
        # Only process the root after the right subtree has been processed
        diameter_tree = 0
        return_values = []
        postorder = [(root, False)]
        while postorder:
            node, right_subtree_processed = postorder.pop()
            if node:
                if right_subtree_processed:
                    # 1. The diameter with this node as the root of the subtree
                    right_subtree_longest_path = return_values.pop()
                    left_subtree_longest_path = return_values.pop()
                    local_diameter = left_subtree_longest_path + right_subtree_longest_path

                    diameter_tree = max(diameter_tree, local_diameter)

                    # 2. The longest path from a leaf node passing through this node, enroute to the route
                    return_values.append(max(left_subtree_longest_path,
                                             right_subtree_longest_path) + 1)
                else:
                    postorder.append((node, True))
                    postorder.append((node.right, False))
                    postorder.append((node.left, False))
            else:
                return_values.append(0)

        return diameter_tree

    def diameterOfBinaryTree_rec(self, root: Optional[TreeNode]) -> int:
        diameter_tree = 0
        # S.C. - O(N) - Unbalanced
        #        O(logN)  Balanced

        # T.C. - O(N)
        def postorder(node):
            nonlocal diameter_tree

            if node == None:
                return 0

            left_subtree_longest_path = postorder(node.left)
            right_subtree_longest_path = postorder(node.right)

            # 1. The diameter with this node as the root of the subtree
            local_diameter = left_subtree_longest_path + right_subtree_longest_path

            diameter_tree = max(diameter_tree, local_diameter)

            # 2. The longest path from a leaf node passing through this node
            return max(left_subtree_longest_path, right_subtree_longest_path) + 1

        postorder(root)
        return diameter_tree
