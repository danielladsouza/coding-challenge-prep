# LC 978 - 978. Longest Turbulent Subarray

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        Test cases - [3, 8, 2] Peak
                     [8, 3, 7] Valley
                            |
                     [3, 8, 8, 9]
                     [3, 8]
                     [8, 3]
                     [3, 3]

        9
         \
          \
           4  -    3

        arr[k-2] < arr[k-1] > arr[k]
        arr[k-2] > arr[k-1] < arr[k]

        k > = 2

        [4]
        [4, 4]

        k > = 1
            len = 2

        else
            len = 1


        If the element is part of a peak / valley, we increment the len of the turbulent
        subarray

        Look at the prev element >= 1, if different
        2

        len = 1
        """
        current_len = 0
        max_len = 0

        for k in range(len(arr)):
            if k >= 2 and ((arr[k] > arr[k - 1] < arr[k - 2]) or
                           (arr[k] < arr[k - 1] > arr[k - 2])):
                current_len += 1
            elif k >= 1 and arr[k] != arr[k - 1]:
                current_len = 2
            else:
                current_len = 1

            max_len = max(max_len, current_len)

        return max_len