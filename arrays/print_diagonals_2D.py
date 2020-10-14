""" Given a 2D grid (4 x 4)
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
Expected output - 1 2 3 4
                  4 3 2 1

Clarify - Is it safe to assume that the grid is an N X N grid
          Can we assume that the grid is never empt

"""

from typing import List

def print_diagonals(nums:List[List[int]])->None:
	if not nums:
		return
	for i in range(len(nums)):
		print(nums[i][i], end= ' ')
	print('\n')
	
	for i, j in zip(range(len(nums)), range(len(nums)-1,-1,-1)):
		print(nums[i][j], end=' ')

nums = [[1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4]]

print_diagonals(nums)
