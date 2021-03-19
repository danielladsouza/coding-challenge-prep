"""
    LC 23. Merge k Sorted Lists
    https://leetcode.com/problems/merge-k-sorted-lists/

    CAVEAT - Unable to modify ListNode class in leetcode
    Hence this solution throws an error with regards to comparing two ListNode
    classes
"""

import heapq


from typing import List, Tuple


class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Custom compare method
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    """
        Time Complexity O(nlogk)
        n - total number of nodes
        k - length of the matrix / number of rows
        Space Complexity - O(k)
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # Have each element on the heap as a tuple, to customize the heap order
        # min_heap: List[Tuple[int, ListNode]] = []
        min_heap: List[ListNode] = []
        heapq.heapify(min_heap)

        for head in lists:
            # heapq.heappush(min_heap, (head.val, head))
            heapq.heappush(min_heap, head)

        dummy_head = tail = ListNode()

        while min_heap:
            smallest_element = heapq.heappop(min_heap)
            tail.next = smallest_element

            next_element = smallest_element.next
            if next_element is not None:
                heapq.heappush(min_heap, next_element)
            tail = tail.next

        return dummy_head.next

