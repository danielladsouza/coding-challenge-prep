"""
    LC 118 - Pascal's triangle
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
            numRows = 1 [1]
                      2 [1], [1,1]

            1. Result is composed of a concat of a list of numbers
            2. For each row - 0 based ith row -  i+ 1 numbers

            T.C. - To compute each element value O(1) time
            The number of elements increases with each level
            1 + 2 + 3 +..n = n(n+1) / 2 elements as well as operations
            Time and space complexity - O(n**2)
        """
        result = []
        for i in range(numRows):
            result.append([1 for _ in range(i + 1)])

            if i > 1:
                # update the middle element based on the previous row

                for j in range(len(result[i - 1]) - 1):
                    result[i][j + 1] = result[i - 1][j] + result[i - 1][j + 1]

        return result


"""

    numRows = 3
    0, 1, 2 , 3, 4

    0
        [1]
        [1, 1]  <---
        [1, 2, 1]     i = 2
        [1, 1 1]
"""

