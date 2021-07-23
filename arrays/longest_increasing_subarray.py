"""
    Longest Increasing Subarray

    1. Given an integer array nums, return the length of the longest strictly increasing subarray.
    2. Given an integer array nums, return the longest strictly increasing subarray.
    Example 1:

    Input: nums = [10,9,2,3,5,7,18,101]
    Output: 6
    Explanation: The longest increasing subarray is [2,3,5,7,18,101], therefore the length is 6.
    Example 2:

    Input: nums = [0,1,2,3,3,7]
    Output: 4
    Example 3:

    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
     0 1  2
    [2,3,4]

    [2,3]
    [2,3,3]

"""
def longest_increasing_subarray(nums):
    current_max = 0
    global_max = 0

    for k in range(len(nums)):
        if k >= 1 and (nums[k] > nums[k-1]):
            current_max += 1
        else:
            current_max = 1
        global_max = max (current_max, global_max)
    return global_max


assert(longest_increasing_subarray([10,9,2,3,5,7,18,101]) == 6)
assert(longest_increasing_subarray([10, 10, 10]) == 1)
assert(longest_increasing_subarray([10, 9, 10]) == 2)
assert(longest_increasing_subarray([10, 9, 9, 8, 7]) == 1)
assert(longest_increasing_subarray([10, 11, 5]) == 2)


def longest_increasing_sub(nums):
    """
        returns the subarray
    """
    current_max = 0
    global_max = 0
    current_sub = []
    global_sub = []

    for k in range(len(nums)):
        if k >= 1 and (nums[k] > nums[k-1]):
            current_max += 1
            current_sub.append(nums[k])
        else:
            current_max = 1
            current_sub = [nums[k]]

        if current_max > global_max:
            global_max = current_max
            global_sub = current_sub

    return global_sub

assert(longest_increasing_sub([10,9,2,3,5,7,18,101]) == [2,3,5,7,18,101])
assert(longest_increasing_sub([10, 10, 10]) == [10])
assert(longest_increasing_sub([10, 9, 10]) == [9,10])
assert(longest_increasing_sub([10, 9, 9, 8, 7]) == [10])
assert(longest_increasing_sub([10, 11, 5]) == [10, 11])



