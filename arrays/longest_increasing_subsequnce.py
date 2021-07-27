""" L.C. 300. Longest Increasing Subsequence

    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

    Example 1:

    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    Example 2:

    Input: nums = [0,1,0,3,2,3]
    Output: 4
    Example 3:

    Input: nums = [7,7,7,7,7,7,7]
    Output: 1


    Constraints:

    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104
"""

from typing import List

"""
The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            O(nlog(n)) time
            O(n) space
        """
        smallestTail = []
        for num in nums:
            if not smallestTail or num > smallestTail[-1]:
                # num is bigger than everything before it, so make it the tail of a new, longer subsequence.
                smallestTail.append(num)
            else:
                # num is smaller than some of the previous numbers, so it replaces some of the existing subsequences with a smaller tail,
                # making them easier to extend in the future. Use binary search to figure out where num should go.
                a = 0
                b = len(smallestTail) - 1
                while a != b:
                    mid = (a + b) // 2
                    if num > smallestTail[mid]:
                        a = mid + 1
                    else:
                        b = mid
                smallestTail[a] = num

        return len(smallestTail)

    def lengthOfLIS_1(self, nums: List[int]) -> int:
        """
            T.C. - O(N**2)
            S.C. - O(N)

            Longest strictly increasing subsequence

            Characteristic of the subsequence
            for a[i:j]

            a[i+1] > a[i]

            [10,9,2,5,3,7,101,18]
              0 1 2 3 4 5 6    7
                    |
            0.  1
            9.  1 + 0
            2.  1 + 0
            5.  1 + LIS[2] = 2
            3   1 + max(LIS[2]) = 2
            7.  1 + max()

            Algorithm - The length of the LIS ending at index i is 1 + the max(LIS at indices with values less than i)
            Us a pre-allocated array
            Use a generator expression instead of fully materialized list - space efficiency
            Lazy iterable, single use
            max((), default=0) - max will raise a ValueError if the iterable is empty

        """
        lis = [1] * len(nums)
        lis[0] = 1
        for i in range(1, len(nums)):
            lis[i] = 1 + max((lis[j] for j in range(i) if nums[i] > nums[j]),
                             default=0)

        return max(lis)


s = Solution()
nums = [10,9,2,5,3,7,101,18]
result = s.lengthOfLIS(nums)



