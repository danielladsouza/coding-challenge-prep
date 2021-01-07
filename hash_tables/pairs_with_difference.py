"""
    Pairs with Specific Difference
    Given an array arr of distinct integers and a nonnegative integer k,
    write a function findPairsWithGivenDifference that returns an array of all
    pairs [x,y] in arr, such that x - y = k. If no such pairs exist,
    return an empty array.

    Note: the order of the pairs in the output array should maintain the order
          of the y element in the original array.
"""

from typing import List


def find_pairs_with_given_difference(arr: List[int], k : int) -> List[List[int]]:
    """
        Time complexity - O(N)
        Space complexity - O(N)
    """
    result = []

    # Preprocessing - Convert to a hashmap - TC O(N), SC O(N)
    pair_hashmap = {x: 0 for x in arr}

    # Look for my counterpart
    for y in arr :
        if (y + k) in pair_hashmap:   # O(1) - Hashmap
            result.append([y+k, y])

    return result

# Tests


assert find_pairs_with_given_difference([0, -1, -2, 2, 1], 1) ==  \
       [[1, 0], [0, -1], [-1, -2], [2, 1]]
