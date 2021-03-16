"""
    LC 88. Merge Sorted Array
    https://leetcode.com/problems/merge-sorted-array/

    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Algorithm - We will utilize the fact that the two arrays are sorted to save on Time Complexity
and the fact that nums1 has enough space to hold nums2 to save on Space Complexity

Case 1 -

nums1 = [1,2,3,4,5,6]
nums2 = [4,5,6]

nums1 = [1,2,3,4,5,6]
i              |

nums2 = [4,5,6]
j       |

nums1 = [1,2,3,4,4,5,5,6,6]


Case 2 -

nums1 = [1,2,3]
nums2 = [1,2,3,4,5,6]

nums1 = [1,2,3]
i       |

nums2 = [1,2,3,4,5,6]
j        |

nums1 = [1,1,2,2,3,3,4,5,6]

"""
from typing import List


class Solution:
    """
        # TC - O(m + n)
        # SC - O (1)
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 1. Moving elements up from the start of an array is more expensive
        # We will approach this by identifying the largest elements and storing
        # them at the very end of the array nums1

        i = m - 1
        j = n - 1

        max_index = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[max_index] = nums1[i]
                i -= 1
                max_index -= 1
            else:
                nums1[max_index] = nums2[j]
                j -= 1
                max_index -= 1

        if j >= 0:
            # Still have elements in nums2 to be merged.
            for k in range(max_index, -1, -1):    # Counting down
                nums1[k] = nums2[j]
                j -= 1


s = Solution()
n1 = [1,2,3,4,5,6,0,0,0]
n2 = [4,5,6]

s.merge(n1, 6, n2, 3)
print(n1)

n1 = [1,2,3,0,0,0,0,0,0]
n2 = [1,2,3,4,5,6]

s.merge(n1, 3, n2, 6)
print(n1)


