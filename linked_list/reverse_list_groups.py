"""
    EPI 7.2 Reverse a linked list in groups of k elements
"""
from typing import List, Optional

class LinkedListNode:
    def __init__(self, data=0, next_ref=None):
        self.data = data
        self.next = next_ref

# EPI 7.2 v2
# Write a program which takes as input a singly linked list L and a nonnegative
# integer k, and reverses the list k nodes at a time.
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
from typing import Optional


def reverseNodesInKGroups(head: ListNode, k: int):
    """
        Reverse the elements in a linked list in groups of k elements
        T.C. - O(n ** 2)
        The reverse_sublist needs to be optimized so that we do not have to travel all the way to the sublist_head
    """

    check_k_nodes_iter = head
    counter = 0
    last_end = 0
    reversed_list_head = head
    while check_k_nodes_iter:
        counter += 1
        check_k_nodes_iter = check_k_nodes_iter.next

        if counter % k == 0:
            reversed_list_head = reverse_sublist(reversed_list_head,
                                                 last_end + 1, counter)
            last_end = counter

    return reversed_list_head


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # Initialize the dummy_head and the sublist_head

    dummy_head = ListNode(0)
    dummy_head.next = L

    sublist_head = dummy_head

    # Linked list nodes assume are numbered from 1 onwards.
    # Ge to the start - 1 th node
    # sublist_head is the node before your sublist

    # Iterate to the (start - 1)th node.
    for _ in range(1, start):
        sublist_head = sublist_head.next  # 11

    # Reverse the sublist by focussing on the successor fields that need to
    # be updated.

    # Iterate over the sublist
    # The sublist_head.next moves along the sublist . Since we are reversing
    # the linked list - "The first will be last and the last shall be first"

    # The sublist_head is set currently at the start - 1 th ListNode.
    # We are reversing the sublist, so we will need a new sublisthead.next (that corresponds to the last node in the sublist)
    # Note we do not change sublist_head .. This is staying fixed.It is anchored to the node prior to our sublist

    sublist_iter = sublist_head.next  # Assume start - 3, finish - 4 , sublist_iter - 3
    """
      0->1->2->3->4->5->6->7->8->9
      sublist_head - 2
      sublist_head.next needs to ultimately be 4
     """
    for _ in range(finish - start):
        temp = sublist_iter.next  # The next node 5
        sublist_iter.next, temp.next, sublist_head.next = (
        temp.next, sublist_head.next, temp)

    return dummy_head.next


















