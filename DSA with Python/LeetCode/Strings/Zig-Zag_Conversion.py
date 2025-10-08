# PROBLEM NUMBER: 6
# https://leetcode.com/problems/zigzag-conversion/
# Zig-Zag Conversion
# Difficulty: MEDIUM
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # APPROACH:
        # This solution converts a string `s` into a zigzag pattern on `numRows` rows and then reads it line by line.
        # 1. Handle edge cases: if `numRows` is 1 or greater than the length of `s`, return `s` as-is.
        # 2. Initialize a list `rows` with empty strings for each row.
        # 3. Use a variable `curRow` to track the current row and a boolean `goingDown` to track the direction.
        # 4. Iterate through each character in the string:
        #    - Append the character to the current row.
        #    - If the top or bottom row is reached, reverse the direction (`goingDown = not goingDown`).
        #    - Move `curRow` up or down based on `goingDown`.
        # 5. Finally, concatenate all rows using `''.join(rows)` to get the zigzag-converted string.
        # This approach simulates the zigzag traversal efficiently without using a 2D matrix, achieving O(n) time complexity.

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curRow = 0
        goingDown = False

        for char in s:
            rows[curRow] += char
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        return ''.join(rows)