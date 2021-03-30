"""
    EPI 7.2 - reverse singly linked list
"""
from typing import Optional


class LinkedListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def reverse_linked_list(L: LinkedListNode) -> LinkedListNode:
    """
        Time complexity - O(N)
        Space Complexity - O(1)

        11->3->5->7->2

        2->7->5->3->11

        None->11->3->5->7->2
        Iterate over the linked list, updating the successive next references.

    """
    prev = temp = None
    current = L

    while current:
        temp = current.next   # temporary holder for the next
        current.next = prev   # flip
        prev = current
        current = temp

    return prev


node5 = LinkedListNode(2, None)
node4 = LinkedListNode(7, node5)
node3 = LinkedListNode(5, node4)
node2 = LinkedListNode(3, node3)
node1 = LinkedListNode(11, node2)

result = reverse_linked_list(node1)