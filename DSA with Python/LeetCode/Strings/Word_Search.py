# PROBLEM NUMBER: 79
# https://leetcode.com/problems/word-search/
# DIFFICULTY: MEDIUM
# 79. Word Search
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # APPROACH:  
        # This solution uses **Backtracking (Depth-First Search)** to check whether a given word exists in a 2D character grid.
        # 1. Determine the grid dimensions — `rows` and `cols`.
        # 2. Define a recursive helper function `backtrack(r, c, i)`:
        #    - `r`, `c` represent the current cell position.
        #    - `i` represents the current index in the `word`.
        #    - Base Case: If `i` equals the length of `word`, it means the entire word has been found — return True.
        #    - Boundary & Mismatch Check: If the current position is out of bounds or the character does not match `word[i]`, return False.
        # 3. Temporarily mark the current cell as visited (e.g., with `"#"`) to avoid revisiting during the same path.
        # 4. Explore all four possible directions — up, down, left, right — by recursively calling `backtrack`.
        # 5. Restore the cell’s original value after exploring all paths (backtracking step).
        # 6. Iterate through every cell in the board:
        #    - If the cell’s character matches the first letter of the word, call `backtrack` starting from that cell.
        #    - If any call returns True, the word exists in the grid.
        # 7. If no valid path is found, return False.
        # This ensures that all possible paths are explored systematically without revisiting cells in the same path.
        # Time Complexity: O(N * 4^L), where N = total cells in the board, L = length of the word.
        # Space Complexity: O(L) due to recursion depth.
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[i]):
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            
            found = (backtrack(r + 1, c, i + 1) or
                     backtrack(r - 1, c, i + 1) or
                     backtrack(r, c + 1, i + 1) or
                     backtrack(r, c - 1, i + 1))
            
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
        return False