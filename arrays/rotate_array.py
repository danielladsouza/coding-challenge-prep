# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

from typing import List
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Brute force
        #for k count iterations.. k value does not matter here.. just used as a counter
        #rotate the array to the right.
        print(nums)
        # Normalize k 
        k = len(nums) % k

        while k > 0:
            temp = nums[-1]
            for i in range(len(nums)-1, 0, -1):
                nums[i] = nums[i-1]

            nums[0] = temp

            k -=1

        # Time complexity O(k x N)
        # Space Complexity O(1)

        #How can we improve on this?

    """ Rotate the first k elements and the remaining (n - k) elements . Finally """
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        start = len(nums) - k
        
        self.reverse(nums, start, len(nums) - 1)      
        self.reverse(nums, 0, start-1)
        self.reverse(nums, 0, len(nums) - 1)

        # Time complexity - O(3N) --> O(N)
        # Space complexity - O(1)

    def reverse(self, nums: List[int], start: int, end: int):
        """ Reverses a list of numbers in place """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]

            start += 1
            end -= 1

        


        



s = Solution()
nums = [1,2,3,4,5,6,7]
k = 10
s.rotate2(nums, k)
print(nums)


