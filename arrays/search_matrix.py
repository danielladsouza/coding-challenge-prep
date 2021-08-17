"""
    LC 74 Search a 2D Matrix
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # When dealing with sorted arrays, we should use Binary Search
        # It brings down the Time complexity to O(log max(m,n))
        # Identify the row in which the number falls
        # Iterate over column 0 and find i such that row[i][0] <= target <= row[i][0]

        # To search through the m rows, we could use a binary search
        # once we have found the row i, we can identify the column j using a binary search along the row

        m, n = len(matrix), len(matrix[0])

        # Identify i
        # T.C. O(log m)
        left, right = 0, m - 1
        i = 0
        while left <= right:
            i = left + (right - left) // 2
            if matrix[i][0] <= target <= matrix[i][n - 1]:
                break

            if target > matrix[i][n - 1]:
                left = i + 1
            else:
                right = i - 1

        left, right = 0, n - 1
        j = 0
        while left <= right:
            j = left + (right - left) // 2
            if target == matrix[i][j]:
                break
            if target > matrix[i][j]:
                left = j + 1
            else:
                right = j - 1

        if matrix[i][j] == target:
            return True
        return False

    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        """
            Flatten out the 2D array and you will see that the data is sorted
            We will work with the flattened array and use Binary search to find the target
            Watch out for errors calculating the mid in Binary search.
            T.C. O(log mn)
            S.C O(1)
        """
        m = len(matrix)
        n = len(matrix[0])

        # Converting a position in a 2D matrix to 2D coordinates
        def convert_to_2d_idx(x):
            return x // n, x % n

        l = 0
        r = m * n - 1

        i = j = 0

        # Use Binary search as the data is sorted
        while l <= r:
            mid = l + (r - l) // 2  # Protect against overflow

            i, j = convert_to_2d_idx(mid)

            if matrix[i][j] == target:
                break

            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1

        return (matrix[i][j] == target)

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
s = Solution()
result = s.searchMatrix(matrix, target)
print(result)

result = s.searchMatrix_1(matrix, target)
print(result)