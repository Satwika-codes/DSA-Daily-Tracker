# PROBLEM NUMBER:678
# https://leetcode.com/problems/valid-parenthesis-string/
# 678. Valid Parenthesis String
# DIFFICULTY: HARD

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Approach:
        # We need to check if the string is valid considering:
        # • '(' → open bracket
        # • ')' → close bracket
        # • '*' → can be '(', ')' or empty
        #
        # Key Idea:
        # Instead of fixing '*' immediately, we track a RANGE
        # of possible open brackets using two variables:
        #
        # • low  → minimum possible open brackets
        # • high → maximum possible open brackets
        #
        # Step 1: Initialize low = 0, high = 0
        #
        # Step 2: Traverse the string:
        #
        # Step 3: For each character:
        #
        #   If '(':
        #       • low += 1
        #       • high += 1
        #
        #   If ')':
        #       • low -= 1
        #       • high -= 1
        #
        #   If '*':
        #       • low -= 1   (treat '*' as ')')
        #       • high += 1  (treat '*' as '(')
        #
        # Step 4: If high < 0:
        #         • Too many ')' → invalid
        #
        # Step 5: If low < 0:
        #         • Reset low = 0
        #           (because we can treat '*' as empty)
        #
        # Step 6: At end:
        #         • Valid if low == 0

        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            if high < 0:
                return False

            if low < 0:
                low = 0

        return low == 0