"""
    Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

    Example

    For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
    containsCloseNums(nums, k) = true.

    There are two 2s in nums, and the absolute difference between their positions is exactly 3.

    For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
    containsCloseNums(nums, k) = false.

    The absolute difference between the positions of the two 2s is 3, which is more than k.

    Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer nums

    Guaranteed constraints:
    0 ≤ nums.length ≤ 55000,
    -231 - 1 ≤ nums[i] ≤ 231 - 1.

    [input] integer k

    Guaranteed constraints:
    0 ≤ k ≤ 35000.

    [output] boolean

"""
from collections import defaultdict

def containsCloseNums(nums, k):
    """
        Find duplicates - tuple (index positions)
        The first one that you find, return i, j

        nums = [0,1,2,3,5,2] k = 3

        2 - 5 = 3
        True

        nums = [0,2,2,3,5,2] k = 3

        can the array contain duplicate numbers

        nums_map
        value [positions]

        As we add values to the map , we can compare the index positions to see if they match k

        abs(i - j) < = k
        abs(i - k) <= j

        T.C. - O(N**2)
        S.C. - O(N)
    """
    nums_map = defaultdict(set)

    for i, v in enumerate(nums):
        for j in nums_map[v]:
            if abs(i - j) <= k:
                return True

        nums_map[v].add(i)

    return False
