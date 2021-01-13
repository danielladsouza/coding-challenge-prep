"""
linked_list_API.py implements API for search, insert and delete
"""

class ListNode:
    def __init__(self, data=0, next_ref=None):
        self.data = data
        self.next = next_ref


def search_list(head: ListNode, key: int) -> ListNode:
    """
    Test cases
    1. Empty list
    2. 1 node in list
    3. Multiple nodes in list
    """
    current = head
    while current:
        if current.data == key:
            return current
        current = current.next

    return current


def search_list_2(current: ListNode, key: int) -> ListNode:
    """
    Test cases
    1. Empty list
    2. 1 node in list
    3. Multiple nodes in list
    Two conditions under which we keep iterating
    We will either reach the end of the list or will find the node.
    """
    while current and current.data != key:
        current = current.next

    return current




