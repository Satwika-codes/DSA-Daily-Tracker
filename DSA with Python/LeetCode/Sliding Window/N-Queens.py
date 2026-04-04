# PROBLEM NUMBER: 51
# https://leetcode.com/problems/n-queens/
# 51. N-Queens
# DIFFICULTY: HARD
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # Approach:
        # We need to place n queens on an n x n board such that:
        # • No two queens attack each other
        # • That means no same column, same row, or same diagonal
        #
        # Step 1: Use backtracking to try placing queens row by row.
        #
        # Step 2: Maintain three sets to track unsafe positions:
        #         • cols → columns where queens are already placed
        #         • diag1 → (r - c) diagonals
        #         • diag2 → (r + c) diagonals
        #
        # Step 3: Start placing queens from row 0.
        #
        # Step 4: For each row r, try all columns c:
        #         • If column or diagonals are already occupied → skip
        #
        # Step 5: If safe:
        #         • Place queen at (r, c)
        #         • Mark column and diagonals as used
        #
        # Step 6: Move to next row (recursive call)
        #
        # Step 7: If all rows are filled (r == n):
        #         • Convert board to required format
        #         • Add it to result
        #
        # Step 8: Backtrack:
        #         • Remove queen from (r, c)
        #         • Unmark column and diagonals
        #
        # Step 9: Continue exploring all possibilities

        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                # place queen
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                backtrack(r + 1)

                # backtrack
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return res