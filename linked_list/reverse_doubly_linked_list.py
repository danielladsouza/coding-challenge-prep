"""
    EPI 7.1.V - reverse doubly linked list
"""
from typing import Optional


class LinkedListNode:
    def __init__(self, data=0, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


def reverse_linked_list(L: Optional[LinkedListNode]) -> \
        Optional[LinkedListNode]:
    """
        Time complexity - O(N)
        Space Complexity - O(1)

        Doubly linked list
        None->11->3->5->7->2

        prev  current temp

        Initialize
            prev = temp = None
            current = L  - Head

            Iterate till we have flipped the last node
            while current:
                temp = current.next  # Getting ready to flip
                current.next = current.prev
                current.prev = temp

            What does this look like

            what do we return
            return prev (as current would have moved past the end of the list)
        Goal is
        2->7->5->3->11->None

        None->11->3->5->7->2
        Iterate over the linked list, updating the previous successive
        references.

    """
    prev = temp = None
    current = L

    while current:
        temp = current.next   # temporary holder for the next
        current.next = current.prev  # flip
        current.prev = temp
        prev = current
        current = temp

    return prev


node5 = LinkedListNode(2)
node4 = LinkedListNode(7)
node3 = LinkedListNode(5)
node2 = LinkedListNode(3)
node1 = LinkedListNode(11)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

result = reverse_linked_list(node1)
