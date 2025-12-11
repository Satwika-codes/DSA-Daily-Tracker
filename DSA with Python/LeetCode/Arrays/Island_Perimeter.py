# PROBLEM NUMBER: 463
# https://leetcode.com/problems/island-perimeter/
# 463. Island Perimeter
# DIFFICULTY: EASY
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # APPROACH
        # Step 1: Initialize perimeter to 0.
        # Step 2: Traverse each cell in the grid.
        # Step 3: For each land cell (grid[r][c] == 1):
        #           - Add 4 to perimeter (each land cell has 4 sides).
        #           - Check for shared edges with adjacent land cells:
        #               • If there is a land cell above, subtract 2 (shared edge)
        #               • If there is a land cell to the left, subtract 2 (shared edge)
        # Step 4: After checking all cells, return the total perimeter.
        # --------------------------------------------

        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Each land cell initially contributes 4 to perimeter
                    perimeter += 4
                    # Shared edge with land cell above
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    # Shared edge with land cell to the left
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2

        return perimeter
