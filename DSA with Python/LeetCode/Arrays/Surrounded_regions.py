# PROBLEM NUMBER: 130
# https://leetcode.com/problems/surrounded-regions/
# 130. Surrounded Regions
# DIFFICULTY: MEDIUM
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # Approach:
        # This problem asks us to capture surrounded regions:
        # Convert all 'O' that are completely surrounded by 'X' into 'X'.
        # But 'O' on the border OR connected to a border 'O' should NOT be flipped.
        #
        # Key Idea:
        # - Border 'O's are safe. Any region connected to them must also stay 'O'.
        # - So, we mark all safe 'O's by DFS from the border.
        #
        # Steps:
        # 1. Traverse the border cells (first row, last row, first col, last col).
        # 2. Whenever we find an 'O', run DFS and temporarily mark them as 'T'
        #    to indicate they should NOT be flipped.
        # 3. After marking:
        #       - Any 'O' remaining inside must be surrounded → convert them to 'X'.
        #       - Convert all temporary 'T' marks back to 'O'.
        #
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n) worst case for DFS stack.

        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # Step 1: DFS from all border 'O's
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        # Step 2: Flip surrounded 'O' → 'X' and restore 'T' → 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
