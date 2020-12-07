# 876. Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.

# 1. Listen - singly linked list
# Traverse the list , precomputation, hashmap(key = position, value - ListNode)
# Keep track of the total length of the linked list - n
# Note how middle is calculated - middle of the linked list ceil ((n + 1) / 2) 
# n - 5. , 6 / 2 = 3
# n - 12, 13 / 2 = 6.5.  - ceil -- 7
# return hashmap[middle_index]
# Time Complexity - O(N)
# Space Complexity - O(N)

import math
from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


# Solution 2
# Solution:
# Define a "fast" pointer which will iterate 2 steps at a time over the linked list.
# On every "fast" iteration move "slow" pointer 1 step right.
# When "fast" reaches the end of the linked list, "head" will be the middle.
# Time: O(n)
# Space: O(1)  - Improves on Space Complexity
# Since fast advances 2 steps ahead, by the time it reaches the end of the sequence, slow is 1/2 steps behind. giving you the middle node
# at slow
"""
[1,2,3,4,5,6,7,8,9,10,11]

fast slow
1     1
3     2
5     3
7     4
9     5
11    6
"""
def middleNode_2(self, head: ListNode) -> ListNode:
        
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow
