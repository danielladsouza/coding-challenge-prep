""" Given a 2D grid (4 x 4)
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
Expected output - 1 2 3 4
                  4 3 2 1

Clarify - Is it safe to assume that the grid is an N X N grid - No.. It could be a M X N grid
          Can we assume that the grid is never empty - No.. We need to accomodate for that

1234
1234

Expected output - 1 4
                  4 1
"""

from typing import List

def print_diagonals(nums:List[List[int]])->None:
    rows = len(nums)
    if not rows:
        return
    cols = len(nums[0])
    if rows == cols:
        print_diagonals_square(nums)
    else:
        print_diagonals_rect(nums)

def print_diagonals_square(nums:List[List[int]])->None:
	if not nums:
		return
	rows = len(nums)
	cols = len(nums[0])
	for i, j in zip(range(rows), range(cols)):
		print(nums[i][j], end= '  ')
	print('\n')
	
	for i, j in zip(range(rows), range(cols - 1,-1,-1)):
		print(nums[i][j], end='  ')

def print_diagonals_rect(nums:List[List[int]])->None:
    rows = len(nums)
    if not rows:
        return
    cols = len(nums[0])

    print('\n')
    
    for row, col in zip([0, rows - 1], [0, cols - 1]):
        print(nums[row][col], end= ' ')

    print('\n')
    for row, col in zip([0, rows - 1], [cols-1, 0]):
        print(nums[row][col], end= ' ')

    print('\n')


nums1 = [[1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4]]

nums2 = [[1,2,3,4],
        [1,2,3,4]]

print_diagonals(nums1)

print_diagonals(nums2)

