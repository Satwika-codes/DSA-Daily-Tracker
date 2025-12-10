# PROBLEM NUMBER: 63
# https://leetcode.com/problems/unique-paths-ii/
# 63. Unique Paths II
# DIFFICULTY: MEDIUM
class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # Approach:
        # Step 1: We use 1D DP where dp[j] represents the number of ways to reach cell (i, j)
        #         in the current row.
        #
        # Step 2: Initialize dp[0]:
        #         • If starting cell is blocked → no paths (dp[0] = 0)
        #         • Else → dp[0] = 1
        #
        # Step 3: Traverse the grid row by row:
        #         For each cell:
        #           • If it's an obstacle → dp[j] = 0 (no way to reach it)
        #           • Else:
        #               - If j > 0, add ways from left: dp[j] += dp[j - 1]
        #
        # Step 4: dp[j] always contains valid paths because previous row updates
        #         carry forward automatically.
        #
        # Step 5: The answer is dp[n-1] (bottom-right cell).

        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = 1 if grid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[-1]
