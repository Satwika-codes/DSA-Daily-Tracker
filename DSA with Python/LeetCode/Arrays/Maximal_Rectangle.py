# PROBLEM NUMBER: 85
# https://leetcode.com/problems/maximal-rectangle/
# 85. Maximal Rectangle
# DIFFICULTY: HARD
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # ----------------------------------------------------
        # APPROACH — HISTOGRAM + MONOTONIC STACK
        # ----------------------------------------------------
        # 1. Treat each row of the matrix as the base of a histogram.
        #    - If matrix[r][c] == "1", increase height[c] by 1.
        #    - If it's "0", reset height[c] = 0.
        #
        # 2. For each updated "heights" array, compute the
        #    largest rectangle in the histogram using a
        #    monotonic increasing stack (same logic as LC 84).
        #
        # 3. For each index i:
        #      - While current height < height at stack top:
        #            pop the top -> this gives the height of a rectangle.
        #            width = i - leftBoundary - 1
        #      - Push current index.
        #
        # 4. Take maximum area over all rows.
        #
        # Time Complexity:  O(m * n)
        # Space Complexity: O(n)
        #
        # NOTE:
        # The trick is extending the histogram logic row-by-row.
        # ----------------------------------------------------

        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        res = 0

        for row in matrix:

            # Update histogram heights
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0

            # Compute largest rectangle in histogram
            stack = []
            for i in range(cols + 1):
                h = heights[i] if i < cols else 0  # sentinel 0 height at end

                while stack and h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    res = max(res, height * width)

                stack.append(i)

        return res
