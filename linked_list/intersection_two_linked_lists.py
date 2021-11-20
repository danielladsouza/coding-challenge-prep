"""
    LC 160. Intersection of Two Linked Lists
    Based on Floyd's algorithm. Create a cycle using the second list.
    Iterate over the modified linked list starting at the head of the first linked list
    If the two lists intersect, return the intersection node
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# T. C. O(N)
# S. C. O(1)

class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        """
            A linked list A will have a cycle if A intersects B
            Now if there is a cycle, we can determine the beginning node of the cycle, using Floyd's algorithm
        """
        # 1 - Connect headB to tailB
        current = headB
        prev = None
        while current:
            prev, current = current, current.next

        # prev is at the tail node
        prev.next = headB  # Created the loop

        # 2 Detect the cycle and it's start
        slow = fast = headA

        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                slow = headA
                while slow is not fast:
                    slow, fast = slow.next, fast.next
                # linked lists must retain their original structure after the function returns.
                prev.next = None
                return slow

        prev.next = None
        return None


