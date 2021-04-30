"""
    L.C. 1260. Shift 2D Grid - https://leetcode.com/problems/shift-2d-grid/
    shift_2D.py

    Translate the requirements
    Work through the test cases.
    Share the brute force solution - Time Complexity
    Share an Algorithm
    Reasoning for the approach.

"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift_helper():
            temp = grid[len(grid) - 1][len(grid[0]) - 1]
            i = len(grid) - 1
            j = len(grid[0]) - 1

            while i >= 0 and j >= 0:
                if j == 0:
                    if i == 0:
                        grid[i][j] = temp
                        break  # We are done
                    else:
                        grid[i][j] = grid[i - 1][len(grid[0]) - 1]
                        i = i - 1
                        j = len(grid[0]) - 1
                else:
                    grid[i][j] = grid[i][j - 1]
                    j = j - 1

        for _ in range(k):
            shift_helper()
        return grid


matrix = [[3,8,1,9],
          [19,7,2,5],
          [4,6,11,10],
          [12,0,21,13]]
k = 1

shift_2D(matrix, k)
print(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
k = 9

shift_2D(matrix, k)
print(matrix)

