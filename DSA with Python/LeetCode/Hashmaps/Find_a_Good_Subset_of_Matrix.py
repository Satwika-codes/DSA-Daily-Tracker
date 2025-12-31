# PROBLEM NUMBER: 2421
# https://leetcode.com/problems/find-a-good-subset-of-matrix/
# 2421. Find a Good Subset of Matrix
# DIFFICULTY: HARD
class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        """
        APPROACH:
        - A subset of rows is good if for every column, at most one selected row
          has a value of 1.
        - Represent each row as a bitmask.
        - If a row has all zeros, it alone forms a valid subset.
        - Otherwise, try all pairs of rows and check if their bitmasks do not
          overlap (bitwise AND equals zero).
        - Return the indices of the first valid subset found.
        """

        m, n = len(grid), len(grid[0])
        masks = {}

        for i in range(m):
            mask = 0
            for j in range(n):
                if grid[i][j] == 1:
                    mask |= (1 << j)

            if mask == 0:
                return [i]

            for prev_mask, idx in masks.items():
                if mask & prev_mask == 0:
                    return [idx, i]

            masks[mask] = i

        return []
