from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# Every node in the binary has a constraint. 
# If the range of values stored in a tree are in the range [l, u]
# and we have a root node with a value w, then it's immediate node to it's left will have an upper bound of itself.
# and it's immediate node to it's right will have a lower bound of itself.
# meaning the root node could have a constrainter [l, u] , it's left child has a constraint [l, v] and it's right child 
# has a constraint [v, u], where v is the value at the tree node.
# We can start with setting l and u to -inf and inf respectively
# We are using BFS, explore the immediate neighbors first. For a BFS we will need a queue. Collections.deque provide a list like interface
# with easy access to updates at either end of the list.
from collections import namedtuple
from collections import deque

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    # QueueEntry corresponds to each visited node
    if not tree:
        return True
    
    QueueEntry = namedtuple('QueueEntry', ['node', 'lower', 'upper'])

    bfs_queue = deque([QueueEntry(tree, float('-inf'), float('inf'))])
    entry = None
    while bfs_queue:
        # Process entries in the order they were inserted, left comes first.
        entry = bfs_queue.popleft()
        if entry.node:
            if not (entry.node.data >= entry.lower and entry.node.data <= entry.upper):
                return False

            bfs_queue.extend([QueueEntry(entry.node.left, entry.lower, entry.node.data),
                                QueueEntry(entry.node.right, entry.node.data, entry.upper)])
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
