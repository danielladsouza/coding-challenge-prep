"""
    L.C. 283 Move zeroes
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        To minimize the total number of operations.. Linear time complexity O(N)
        Iterate over the array. Keep track of the current write index
        write_index = 0
        If you come across a non zero element , set the value at the write index to that
        of the non zero element, update the write_index

        0 1 0 3 12
        1 3 12 0 0

        len(nums) - write index .. set to zero
        T.C. O(N)
        S.C. O(1)
        """
        write_index = 0

        for n in nums:
            if n:
                nums[write_index] = n
                write_index += 1

        nums[write_index:] = [0] * (len(nums) - write_index)

        """
        Dry run
        write_index    array
        0              0 1 0 3 12
        1              1 1 0 3 12 
        2              1 3 0 3 12  
        3              1 3 12 3 12        
                              0  0          
        """

