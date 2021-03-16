"""
    https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
    378. Kth Smallest Element in a Sorted Matrix
    Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

    Note that it is the kth smallest element in the sorted order, not the kth distinct element.

    Input: matrix =
    [[ 1, 5, 9],
     [10,11,13],
     [12,13,15]],
    k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

    1, 5, 9, 10, 11 12 13 13 15

"""
from typing import List, Tuple
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
            We will use the information that elements are in sorted order in a row
            as well as a column to get the kth smallest element.
            A min_heap will be used to get the smallest element visited.
        """
        min_heap: List[Tuple[int, int]] = []
        heapq.heapify(min_heap)

        # Create an array of the iterators of each of the sorted rows
        sorted_rows_iters = [iter(x) for x in matrix]

        # We know that the first column should contain the smallest elements
        # per row. We initialize the min_heap with those values

        for i, it in enumerate(sorted_rows_iters):
            first_element = next(it)
            heapq.heappush(min_heap, (first_element, i))

        # Now we start identifying the smallest of the elements in the heap
        count = 0
        # TC klog(m) - m is the number of rows
        # min_heap has at the most m elements at a time
        smallest_element = float('-inf')

        while min_heap and count < k:
            smallest_element, sorted_row_i = heapq.heappop(min_heap)
            count += 1
            sorted_row_iter = sorted_rows_iters[sorted_row_i]
            next_element = next(sorted_row_iter, None)
            if next_element is not None:
                heapq.heappush(min_heap, (next_element, sorted_row_i))

        return smallest_element


m = [[1,5,9],
     [10,11,13],
     [12,13,15]]

s = Solution()

v = s.kthSmallest(m, 8)
print(v)
assert(v == 13)

