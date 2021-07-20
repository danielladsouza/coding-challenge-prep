"""Given a list of numbers, the task is to write a
Python program to find the second largest number in given list.
Examples:

Input: list1 = [10, 20, 4]
Output: 10

Input: list2 = [70, 11, 20, 4, 100]
Output: 70
Method
1: Sorting (nlogn) is an easier but less optimal method.Given below is an
O(n) algorithm to do the same.
"""

# Python program to find second largest
# number in a list

# list of numbers - length of
# list should be at least 2
# list1 = [10, 20, 4, 45, 99]

from typing import List

def find_second_max(list1: List[int]) -> int:
    """
        Time Complexity O(N)
        Space Complexity O(1)
    """
      if len(list1) < 2:
        raise('Length is less than 2. Need at least 2 elemnts')
      # [10,20]
      first_max = max(list1[0], list1[1])
      second_max = min(list1[0], list1[1])

      # [10, 20, 20, 15, 15, 10, 20]
      for i in range(2, len(list1)):
        if list1[i] > first_max:
            second_max, first_max = first_max, list1[i]
        elif list1[i] > second_max  and list1[i] != first_max:
            second_max = list1[i]
      return second_max

list1 = [10,20,4,99, 45,45,45, 99, 99, 101, 100]
print("Second highest number is : ", find_second_max(list1))

