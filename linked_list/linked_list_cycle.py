"""
    LC 141 . Linked List Cycle

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
            Time Complexity - Worst case .. no cycles O(N)
            Space Complexity - O(1)
        """
        if not head:
            return False

        slow, fast = head, head.next

        while fast and fast.next:
            if fast == slow:  # start off at different nodes
                return True
            fast, slow = fast.next.next, slow.next  # fast advances 2 nodes

        return False


"""
    Brute force approach 
    seen = collections.defaultdict(bool)

    while head;
        if head.next in seen;
            return false
        seen[head] = True

    return False

    # O(n) Space complexity ..

    Use a two pointer approach , fast and slow pointer.
    The idea is that if there is a cycle, then the fast and slow pointers will
    collide at some point.
"""