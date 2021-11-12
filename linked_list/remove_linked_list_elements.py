"""
    LC 203 Remove Linked List Elements
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#  T.C. O(N)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[
        ListNode]:
        """
            [4,2,6,3,4,5,6] 1
             X X              6
            [1,1,1,5,1,1,1] 1 - None
          0        X
        """
        dummy = prev = ListNode(0, head)
        current = head

        # Advance along the list looking for a val
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current

            current = current.next
        return dummy.next