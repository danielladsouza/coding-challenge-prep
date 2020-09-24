# EPI 9.2 - Test if a binary tree is symmetric

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# A binary tree is symmetric, if the left subtree is a 'mirror' image of the right subtree
def is_symmetric(tree: BinaryTreeNode)-> bool:
    # TODO - you fill in here.
    if not tree:
        return True

    def check_symetric(subtree_1, subtree_2):
        if not subtree_1 and not subtree_2:
            return True

        if subtree_1 and subtree_2:
            return (subtree_1.data == subtree_2.data and
                    check_symetric(subtree_1.left, subtree_2.right) and
                    check_symetric(subtree_1.right, subtree_2.left))
        else:
            return False # one of the subtrees is None

    return check_symetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
