"""
    L.C. 1351 - Count Negative Numbers in a Sorted Matrix
"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
            R.H. The clearest, least error-prone way of specifying reverse iteration is to specify it
            in a forward direction and then say reversed.
            T.C. O(mn)
            S.C. O(1)
        """
        count = 0
        m, n = len(grid), len(grid[0])
        # Iterate over the columns per row in reverse order, until you find a number that is >= 0
        for i in range(m):
            for j in reversed(range(n)):
                if grid[i][j] < 0:
                    count += 1
                else:
                    break
        return count