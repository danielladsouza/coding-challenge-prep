"""
    LC 23. Merge k Sorted Lists
    https://leetcode.com/problems/merge-k-sorted-lists/

    New solution assuming we cannot modify the LeetCode class.

    To deal with the problems of sort stability and elements with equal priority
    (equal values), the solution is to have each element in the heapq be a tuple
    with the priority, an entry count and the element (ListNode) to be inserted. The entry
    count ensures that elements with the same priority are sorted in the order they
    were added to the heapq.

"""

import heapq
from typing import List, Tuple


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
        min_heap: List[Tuple[int, int, ListNode]] = []

        heapq.heapify(min_heap)

        count = 0
        for head in lists:
            count += 1
            heapq.heappush(min_heap, (head.val, count, head))

        dummy_head = tail = ListNode()

        while min_heap:
            _, _, smallest_element = heapq.heappop(min_heap)
            tail.next = smallest_element
            next_element = smallest_element.next
            if next_element is not None:
                count += 1
                heapq.heappush(min_heap, (next_element.val, count,
                                          next_element))
            tail = tail.next

        return dummy_head.next


