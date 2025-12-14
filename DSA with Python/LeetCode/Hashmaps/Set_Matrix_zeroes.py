# PROBLEM NUMBER: 73
# https://leetcode.com/problems/set-matrix-zeroes/
# 73. Set Matrix Zeroes
# DIFFICULTY: MEDIUM
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # Traverse the entire matrix to record which row and column contains zero
        # Store row indices in one set and column indices in another set
        # This avoids modifying the matrix while scanning and prevents cascading zeros
        # After recording, iterate again and set cells to zero if row or column is marked
        # Using sets ensures O(1) lookup and keeps the logic clean

        m, n = len(matrix), len(matrix[0])
        rows = set()
        cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
