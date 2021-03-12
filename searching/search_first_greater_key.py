"""
    Design an efficient algorithm that takes a sorted array and a key, and
    finds the index of the first occurrence of an element greater than the key.

"""
from typing import List


def search_first_greater_key(arr: List[int], key: int) -> int:
    left, right, result = 0, len(arr) -1, -1

    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] <= key:
            left = mid + 1
        else:
            result = mid
            right = mid - 1

    return result


A = [-14, -10, 2, 109, 110, 243, 285, 285, 285, 401]

assert (search_first_greater_key(A, 285) == 9)

assert (search_first_greater_key(A, -13) == 1)

assert (search_first_greater_key(A, 255) == 6)

assert (search_first_greater_key(A, 108) == 3)



