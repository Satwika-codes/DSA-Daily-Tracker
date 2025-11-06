# PROBLEM NUMBER: 64
# https://leetcode.com/problems/minimum-path-sum/
# 64. Minimum Path Sum
# DIFFICULTY: MEDIUM
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Approach:
        # - Use **Dynamic Programming (DP)** to compute the minimum path sum from top-left to bottom-right.
        # - Modify the `grid` in place to store the minimum sum up to each cell.
        # - For each cell `(i, j)`:
        #   • If it's the first cell (0,0), keep it as is.  
        #   • If in the first row, it can only come from the left (`grid[i][j] += grid[i][j-1]`).  
        #   • If in the first column, it can only come from above (`grid[i][j] += grid[i-1][j]`).  
        #   • Otherwise, it can come from either top or left — choose the smaller (`grid[i][j] += min(grid[i-1][j], grid[i][j-1])`).  
        # - The last cell (`grid[m-1][n-1]`) will contain the minimum path sum.
        # Time: O(m * n)   Space: O(1) (in-place DP)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]