# L.C. 695 Max Area of Island
# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
            Iterate over each cell in the grid
            If you encounter a 1 then check it's neighbors (BFS) for 1's)
            While you have 1's in it's frontier, keep exploring
            Thus you will get the area of the island

            Keep track of the max_area= max(local_area, max_area)
            Also keep tracks of the cells that you have already seen.
            T.C. - O(MN) Visit each cell just once.
            S.C. - O(MN) Keeping track of cells that have been visited
        """

        def get_neighbors(a, b, seen):
            result = []

            neighbor_offset = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for n in neighbor_offset:
                if 0 <= (a + n[0]) < len(grid) and 0 <= (b + n[1]) < len(
                        grid[0]):
                    if grid[a + n[0]][b + n[1]] and (
                    a + n[0], b + n[1]) not in seen:
                        result.append((a + n[0], b + n[1]))

            return result

        seen = set()
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in seen:
                    continue

                seen.add((i, j))
                if not grid[i][j]:
                    continue

                frontier = [(i, j)]
                local_area = 0

                while frontier:
                    a, b = frontier.pop()
                    local_area += 1

                    neighbors = get_neighbors(a, b, seen)

                    for n in neighbors:
                        frontier.append(n)
                        # Do not process this cell again
                        seen.add(n)

                max_area = max(max_area, local_area)

        return max_area