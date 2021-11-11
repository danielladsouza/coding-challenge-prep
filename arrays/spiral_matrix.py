"""
    LC 54 - Spiral Matrix
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
            (0,1) (1,0), (0,-1) (-1,0)
            Right. Down.   Left   Up

            Start at 0,0, traverse the matrix using some rules

            Keep track of the cells we have already visited. - None

            (0,0)

            visiting neigbors to the Right
            RIGHT
            Reach the end of the columns
            DOWN
            REach the end of the rows
            LEFT
            Reach past the start of the row
            UP or encounter a visited cell .. switch direction
            Do this m * n times
            -- Linear Time Complexity O(N)
            Space Complexity O(N)

            Repeat again
        """
        shift = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = x = y = 0
        spiral_matrix = []

        # There are a total of m * n elements
        m = len(matrix)
        n = len(matrix[0])

        for _ in range(m * n):
            spiral_matrix.append(matrix[x][y])
            matrix[x][y] = None  # Mark cell as visited

            next_x, next_y = x + shift[direction][0], y + shift[direction][1]

            if (next_x not in range(m) or
                    next_y not in range(n) or
                    matrix[next_x][next_y] == None):
                # change direction
                direction = (direction + 1) % 4
                next_x, next_y = x + shift[direction][0], y + shift[direction][
                    1]
            x, y = next_x, next_y

        return spiral_matrix