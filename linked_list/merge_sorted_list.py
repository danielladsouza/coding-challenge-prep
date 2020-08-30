# Definition for singly-linked list.
# 21. Merge Two Sorted Lists
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = None
        l3 = None
        
        if l1 == None and l2 == None:
            return None
        
        if l1 == None:
            return l2
        
        if l2 == None:
            return l1
        
        # establish head of the resulting list
        if l1.val < l2.val:
            l3 = l1
            l1 = l1.next
        else:
            l3 = l2
            l2 = l2.next
        
        ans = l3
        
        # Iterate over the list
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next
                
        if l1 == None:
            while l2 != None:
                l3.next = l2
                l3 = l3.next
                l2 = l2.next
        
        if l2 == None:
            while l1 != None:
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
        
        l3.next = None
        
        return ans
