"""
     L.C. 1290 - 1290. Convert Binary Number in a Linked List to Integer
     1290. Convert Binary Number in a Linked List to Integer
     https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
            Space Complexity - O(1)
            Time Complexity - O(N) - N is the number of nodes in the linked list
        """
        # get the count of the nodes
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        result = 0
        current = head
        while current:
            if current.val:
                result += current.val * (2 ** (count - 1))

            current = current.next
            count -= 1

        return result
