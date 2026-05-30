# PROBLEM NUMBER: 856
# https://leetcode.com/problems/score-of-parentheses/
# 856. Score of Parentheses
# DIFFICULTY: MEDIUM

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Approach:
        # We use a stack to keep track of scores
        # at different nesting levels.
        #
        # Scoring Rules:
        #
        # • "()" = 1
        #
        # • AB = A + B
        #   (concatenation)
        #
        # • (A) = 2 * A
        #   (nesting)
        #
        # Step 1:
        # Maintain:
        #
        # • stack
        #   Stores score before entering
        #   a new parenthesis level.
        #
        # • curr
        #   Stores score of current level.
        #
        # Step 2:
        # When '(' is encountered:
        #
        # • Save current score in stack.
        #
        # • Start a new level with score 0.
        #
        # Step 3:
        # When ')' is encountered:
        #
        # Two possibilities:
        #
        # • "()" → score = 1
        #
        # • "(A)" → score = 2 * A
        #
        # This can be handled using:
        #
        # max(2 * curr, 1)
        #
        # Step 4:
        # Add this score to the score
        # stored before entering the level.
        #
        # Step 5:
        # Continue until entire string
        # is processed.
        #
        # Step 6:
        # Return final score.

        stack = []

        # Score of current level
        curr = 0

        for ch in s:

            # Enter new nesting level
            if ch == '(':

                stack.append(curr)

                curr = 0

            # Exit nesting level
            else:

                curr = (
                    stack.pop()
                    + max(2 * curr, 1)
                )

        return curr