"""
    L.C. 2. Add Two Numbers
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
        Space and Time Complexity - O(max(m, n))
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> \
    Optional[ListNode]:
        carryover = 0
        dummy = tail = ListNode(0, None)

        while l1 or l2 or carryover:
            sum_digits = (l1.val if l1 else 0) + (
                l2.val if l2 else 0) + carryover

            carryover = sum_digits // 10
            tail.next = ListNode(sum_digits % 10, None)
            tail = tail.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next