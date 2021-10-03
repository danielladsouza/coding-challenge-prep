"""
    L.C. 1304 - Find N Unique Integers Sum up to Zero
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        """
            Algorithm
            # To get to a sum zero, fill the first half with =ve values
            # the second half with -ve values so that the total is 0

            n = 4.
            0 0 0 0

            Keep track of edge case , n = 1
            T.C. = O(N)
            S.C. = O(1) - Space for the result
        """
        if n == 1:
            return [0]

        result = [0] * n
        result[:n/ /2] = [x for x in range(1, n// 2 + 1)]
        result[-(n // 2):] = [-x for x in range(1, n // 2 + 1)]
        return result

    def sumZero_2(self, n: int) -> List[int]:
        """
            n = 5
            Think of a number line
            -4 -3 -2 -1 0 1 2 3 4 5

            n = 4
            -3 -2 -1 0 1 2 3 4

        """
        return List(range(1-n, n, 2))