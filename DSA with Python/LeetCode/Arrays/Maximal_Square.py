# PROBLEM NUMBER: 221
# https://leetcode.com/problems/maximal-square/
# 221. Maximal Square
# DIFFICULTY: MEDIUM
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # Approach:
        # We want to find the largest square containing only '1's in the matrix.
        #
        # Steps:
        # 1. Use Dynamic Programming with a dp table of size (m+1) × (n+1)
        #    so boundaries become easier to handle.
        #
        # 2. dp[i][j] represents the size of the largest square whose bottom-right
        #    corner is at matrix[i-1][j-1].
        #
        # 3. For every cell that contains '1':
        #       dp[i][j] = 1 + min(
        #                       dp[i-1][j],     # top
        #                       dp[i][j-1],     # left
        #                       dp[i-1][j-1]    # top-left
        #                     )
        #    This ensures that a new square can only expand if all three neighbors
        #    can support forming a larger square.
        #
        # 4. Track the maximum dp value found — it represents the side length
        #    of the largest square.
        #
        # 5. Return area = side * side.
        #
        # Time Complexity: O(m × n)
        # Space Complexity: O(m × n)

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
                    res = max(res, dp[i][j])

        return res * res
