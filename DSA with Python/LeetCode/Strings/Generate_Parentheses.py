# PROBLEM NUMBER: 22
# https://leetcode.com/problems/generate-parentheses/
# 22.Generate Parentheses
# DIFFICULTY: MEDIUM
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # APPROACH:
        # This solution generates all combinations of well-formed parentheses for a given number `n` using backtracking.
        # 1. Initialize an empty list `result` to store valid combinations.
        # 2. Define a recursive function `backtrack(s, open_count, close_count)`:
        #    - `s` keeps the current combination string.
        #    - `open_count` tracks the number of '(' used so far.
        #    - `close_count` tracks the number of ')' used so far.
        # 3. Base case: if the length of `s` equals `2 * n`, append `s` to `result` since a valid combination is formed.
        # 4. Recursive steps:
        #    - If `open_count < n`, add '(' and recurse.
        #    - If `close_count < open_count`, add ')' and recurse.
        # 5. Call `backtrack()` initially with empty string and counts 0.
        # 6. Return `result` containing all valid parenthesis combinations.
        # This approach efficiently explores all valid sequences while pruning invalid paths, achieving O(4^n / √n) time complexity.

        result = []

        def backtrack(s="", open_count=0, close_count=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack()
        return result