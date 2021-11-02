"""
    LC 303 - Range Sum Query - Immutable
"""
import unittest
from typing import List

class NumArray:
    """
        Brute Force - compute the sum at index right, left -1 one every call to sumRange
        T.C. O(N) * 10**4
        O(1)
        nums immutable
        Preprocessing

        Algorithm
        cumulative_sum[i] = cumulative_sum[i - 1] + nums[i]

         [-2, 0, 3, -5, 2, -1
        0 -2. -2 1  -4  -2 -3    (Base offset 1)

        [2.5]  cumulative_sum[i+1] = cumulative_sum[i] + nums[i]
        Prevent out of range, use a sentinel value

        T.C. = O(N). -- initialization
        S.C. = O(N)

        sumRange - O(1)
    )
    """

    def __init__(self, nums: List[int]):
        self._cumulative_sum = [0] * (len(nums) + 1)
        for idx, val in enumerate(nums):
            self._cumulative_sum[idx + 1] = self._cumulative_sum[idx] + val

    def sumRange(self, left: int, right: int) -> int:
        """
            T.C. = O(N)
            S.C. = O(N)
        """
        return self._cumulative_sum[right + 1] - self._cumulative_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class TestNumArray(unittest.TestCase):
    def setUp(self):
        self._num_array = NumArray([-2, 0, 3, -5, 2, -1])

    def test_sum_range_returns_1_given_input_0_2(self):
        self.assertEqual(self._num_array.sumRange(0, 2), 1)

    def test_sum_range_returns_neg_1_given_input_2_5(self):
        self.assertEqual(self._num_array.sumRange(2, 5), -1)

if __name__ == '__main__':
    unittest.main()

