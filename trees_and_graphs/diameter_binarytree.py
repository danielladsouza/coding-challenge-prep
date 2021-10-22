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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
            In Python integers are immutable types
        """

        diameter_tree = 0  # Outer Function scope declaration
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

            # When we are assigning a value to diameter_tree, a new local variable diameter_tree is getting created
            # This is a new variable, different fromt the diameter_tree in the outer scope
            # If we want to be able to use the variable from the outer scope, we need to specifically tell the Interpreter, this
            # is a nonlocal variable.
            # This assignment could cause a new variable to be created, it would be treated as a local variable
            # The Python interpreter sees this at module load time and decides that the global scope's diameter_tree should not be used inside
            # the local scope.

            # This is a question of scope.
            # We will have a scoping issue if we do not use the nonlocal keyword for diameter_tree
            #                       |   <--- this is a local variable in postorder() , but the Python interpreter is unable to see where it was declared
            diameter_tree = max(diameter_tree, local_diameter)


            # 2. The longest path from a leaf node passing through this node
            return max(left_subtree_longest_path, right_subtree_longest_path) + 1

        postorder(root)
        return diameter_tree
