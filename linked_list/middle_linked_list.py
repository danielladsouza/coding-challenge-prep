# 876. Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1. Listen - singly linked list
# Traverse the list , precomputation, hashmap(key = position, value - ListNode)
# Keep track of the total length of the linked list - n
# middle of the linked list ceil ((n + 1) / 2) 
# n - 5. , 6 / 2 = 3
# n - 12, 13 / 2 = 6.5.  - ceil -- 7
# return hashmap[middle_index]
# Time Complexity - O(N)
# Space Complexity - O(N)

from collections import defaultdict
class Solution:
    def __init__(self):
        self.cache = defaultdict(ListNode)
        
    def precompute_nodes(self, head):
        count = 0
        current = head
        while current:
            count += 1
            self.cache[count] = current
            current = current.next
            
        return count
            
    def calculate_middle_index(self, count):
        return math.ceil((count + 1) / 2)
        
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        # 1. Traverse the linked list
        count = self.precompute_nodes(head)
        middle_index = self.calculate_middle_index(count)
        return self.cache[middle_index]