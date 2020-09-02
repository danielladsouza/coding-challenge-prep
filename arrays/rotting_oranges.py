from typing import List
from enum import IntEnum

class CellState(IntEnum):
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        ROTTING = 3
        EXPLORED = 4

class Solution:
    """
        The premise here is we will iterate over the grid and in each iteration we explore a rotten cell , mark it's adjacent neighbors for rotting
        At the end of the iteration we set the rotting cell state to rotten.
        We also try to improve efficiency by only exploring rotten cells that have not been visited in prior iterations
        We are using the CellState enum to keep track of the cell state.
        We know that there are quarantined fresh oranges if we discover them , however they do not make it to the rotting state.
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh_oranges = False
        rotting = []
        rows = len(grid)
        cols = len(grid[0])
        
        # Mark my neighbors for rotting
        def mark_for_rotting(grid, row, col, rotting):
            for dX, dY in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= (row + dX) < rows and 0 <= (col + dY) < cols and grid[row + dX][col + dY] == CellState.FRESH:
                    rotting.append((row + dX, col + dY))
                    grid[row + dX][col + dY] = CellState.ROTTING
                      
        while True:
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == CellState.ROTTEN:
                        mark_for_rotting(grid, row, col, rotting)
                        grid[row][col] == CellState.EXPLORED 
                        
                    if grid[row][col] == CellState.FRESH:
                        fresh_oranges = True
            
            if len(rotting) > 0:
                minutes += 1
                for row, col in rotting:
                    grid[row][col] = CellState.ROTTEN
                fresh_oranges = False
            elif fresh_oranges:
                return -1
            else:
                return minutes

            rotting = []


if __name__ == "__main__":
    s = Solution()
    v = s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    print(v)
