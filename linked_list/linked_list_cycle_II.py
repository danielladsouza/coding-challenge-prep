"""
    LC 142 - Linked List Cycle II

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
    Inputs
    3            No cycle
    3 2          No cycle
    3 2 0        Possibility of having a cycle (We need at least 3 nodes for a cycle to exist)
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
            Time Complexity - Worst case .. no cycles O(N)
            Space Complexity - O(1)
        """
        if not head:
            return False

        slow = fast = head # fast has a headstart

        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:  # Compare identity
                # we have a cycle
                slow = head
                while slow is not fast:
                    slow, fast = slow.next, fast.next
                return slow
        return None

