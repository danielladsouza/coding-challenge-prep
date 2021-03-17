"""
    Given an unsorted array, find the most optimal solution from a space
    and time complexity perspective to get the product of the largest elements in the array

    a = [-1,-4,5,7,21,17,-3,71]

    Result = 71 * 21 = 1420 + 71 = 1491

"""

from typing import List
import heapq


def max_product_1(a : List[int]) -> int:
    if len(a) < 2:
        raise Exception("Invalid length")

    # O(1) space complexity - in place sort
    a.sort(reverse=True)   # TC nlogn
    return a[0] * a[1]


def max_product_2(a : List[int]) -> int:
    """
        Improve on Time Complexity .. can we do better than nlogn
        If we are looking for the largest / smallest elements, a better option
        is to use a heap. A heap has O(log n) time complexity for inserts and
        deletes.
        O(1) time complexity for lookup of the max / min element

        We will use sorting as a preprocessing step to speed up searching
    """
    if len(a) < 2:
        raise Exception("Invalid length of array")

    # O(1) space complexity - in place sort
    # Python heap algorithm is a min_heap. Store the negative value, for
    # max_heap behavior
    a = [(-1) * x for x in a]

    heapq.heapify(a)
    # TC O(logn)
    # This modifies the array. If we want to leave it unchanged..
    return (-1) * heapq.heappop(a) * (-1) * heapq.heappop(a)


def max_product(a : List[int]) -> int:
    """
        Improve on Time Complexity .. can we do better than nlogn
        If we are looking for the largest / smallest elements, a better option
        is to use a heap. A heap has O(log n) time complexity for inserts and
        deletes.
        O(1) time complexity for lookup of the max / min element

        We will use sorting as a preprocessing step to speed up searching
    """
    if len(a) < 2:
        raise Exception("Invalid length of array")

    # O(1) space complexity - in place sort
    # Python heap algorithm is a min_heap. Store the negative value, for
    # max_heap behavior
    print(a)
    a = [(-1) * x for x in a]

    heapq.heapify(a)
    # TC O(logn)
    # This modifies the array. If we want to leave the contents unchanged..
    # The order will change though
    num1 = heapq.heappop(a)
    num2 = heapq.heappop(a)
    heapq.heappush(a, num1)
    heapq.heappush(a, num2)

    a = [(-1) * x for x in a]
    print(a)
    return (-1) * num1 * (-1) * num2


a1 = [-1,-4,5,7,21,17,-3,71]
b = max_product(a1)
print(b)

a2 = []
max_product(a2)


