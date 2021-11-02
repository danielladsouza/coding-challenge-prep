"""
    LC 307 - Range Sum Query - Mutable

"""
from collections import defaultdict


class NumArray:
    """
        Reads - sumRange()

        Writes - update()

        3 * 10 ** 4 - length(nums)

        1. Initialize cumulatie_sum (append a 0 as a sentinel)
        2. sumRange - cumulatie_sum[right + 1] - cumulative_sum[left]

        3. When do we update the cumulative_sum
        4. How do we update it
        We could keep track of the stream of updates

        idx.    0.   1.  2
        nums.   1.   3.  5
        c_sum 0 1.   4.  9

        Updates
        [1,2]
        [1, -3]  <--

        idx.

                -2   -2      -4


        idx        0 1 2   3 4   5

        val        0 1 2   3 4   5          6 7 8 9 10.  (11 numbers)
        cum_sum  0 0 1 3.  6 10 15
                           -4 -4
                               -8
        Update   to    -2 nums[2]

                      -4. idx:
cum_sum_updates       -4.  -4 -4 -4   -(10 - 6) - 4 = -4-4 = -8  Apply to 10

        update   to   -4.  nums[4]
                       -1. 2  6. 11


        How does an update to nums affect cum_sum

        affect on cum_sum[idx + 1]
        old_val = 3
        New_val = -(3 - 1) -2 = -2-2 = -4
        delta ---


                 -1  2
        +2 -2 -2
        cum_sum


        2 + 1 = 3
        -2 + 1 = -1

        -val + update = -2-2 = -4 apply to all the cumulative_sum values past this index
        (2,5)
        left to right
        (0,5)
        Track the changes at various positions[1  -3]


        Optimization
        Apply the changes only if change has occured between indices left and right.
        sort(dictionary), Apply the changes corresonding to keys that fall between left and right.
        clear those from the dictionary.

        1.    2
    """

    def __init__(self, nums: List[int]):
        self._cumulative_sum = [0] * (len(nums) + 1)
        for idx, val in enumerate(nums):
            self._cumulative_sum[idx + 1] = self._cumulative_sum[idx] + val

    """

        2
        1 3 5                       

        0. 1 4 9   cumulative_sum    at index 1 was 4, new cumulative sum at index 1 = 3  (4 - 1) = 3 , 4 - (4-1) + 2 = 4 - 3 + 2 = 1 + 2 = 3
        delta = -(4 - 1) + 2.. apply this delta -1 to all the subsequent cumulative_sum values

          2     nums

          -(4 -1) + 2     new cumulative_sum = 1

          -1                        
    """

    def update(self, index: int, val: int) -> None:
        # How does this input affect the cumulative_sum?
        delta = -(self._cumulative_sum[index + 1] - self._cumulative_sum[
            index]) + val

        for idx in range(index + 1, len(self._cumulative_sum)):
            self._cumulative_sum[idx] += delta

        # Keep track of the delta's to the cumulative_sum

    def sumRange(self, left: int, right: int) -> int:
        # Apply only the delta's from the updates , instead of traversing over the entire nums

        return self._cumulative_sum[right + 1] - self._cumulative_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

