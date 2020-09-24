# EPI # 9.3 Compute the lowest common ancestor in a binary tree
import functools
from typing import Optional
from collections import namedtuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# If I am an ancestor of the two nodes, then the nodes are either present in my left subtree, 
# or in my right subtress, or in either of the two.
# Also I could be one of the nodes. 
# At each node , we can compute, num_nodes_found and ancestor.
# I am an ancestor if the sum of the nodes found in my left and right subtrees as well as taking me
# into consideration is equal to 2.
def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    Status = namedtuple('Status', ['num_nodes_found', 'ancestor'])

    def lca_helper(tree, node0, node1):
        if tree == None:
            return Status(0, None)
        
        left_subtree_status = lca_helper(tree.left, node0, node1)
        if left_subtree_status.ancestor:
            return left_subtree_status

        right_subtree_status = lca_helper(tree.right, node0, node1)
        if right_subtree_status.ancestor:
            return right_subtree_status

        num_nodes_found = left_subtree_status.num_nodes_found + right_subtree_status.num_nodes_found + (node0, node1).count(tree)
        return Status(num_nodes_found, tree if num_nodes_found == 2 else None)

    result = lca_helper(tree, node0, node1)
    return result.ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
