
"""
    LC 852 - Peak Index in a Mountain Array
"""

def peakIndexInMountainArray(self, arr: List[int]) -> int:
    """
      /
     /  \
    /    \


    # Brute Force Approach T.C. O(N), S.C. O(1)
    for idx in range(1, len(arr)):
        if arr[idx] < arr[idx -1]:
            break
    return idx - 1
    """

    # This array is sorted Let's do a binary search
    # T.C. O(logn), S.C. O(1)
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[
            mid + 1]:  # Found the Peak
            break

        if arr[mid] > arr[mid - 1]:
            left = mid + 1
        else:
            right = mid - 1
    return mid