# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            [] - []
            [112] - [12]
            [1222] - [12]
            [1233334] - [1234]
            [44] - 4

        1. Iterate over linked list keeping track of the previous node
        2. if current is duplicate of prev, update prev.next
           Update current to current.next
        3. If curent is not a duplicate, prev = current
           current = current.next

           d 1 1 2
           p c.
             p c
               X  c

             1 2

           Dummy Head float('-inf')
        """
        prev = dummy = ListNode(float('-inf'), head)

        current = head

        while current:
            if current.val == prev.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next