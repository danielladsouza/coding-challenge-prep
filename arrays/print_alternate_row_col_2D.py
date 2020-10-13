from typing import List

def print_alternates(nums: List[List[int]])->None:
    """ Prints alternate rows followed by alternate cols"""
    rows = len(nums)

    if not rows:
	    return

    cols = len(nums[0])


    for row in range(0,rows,+2):
        for col in range(cols):
            print(nums[row][col], end=' ')
        print('\n')

    for col in range(0,cols,+2):
        for row in range(rows):
            print(nums[row][col], end=' ')
        print('\n')



nums = [[1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]]

#nums = [[1]]
print_alternates(nums)


