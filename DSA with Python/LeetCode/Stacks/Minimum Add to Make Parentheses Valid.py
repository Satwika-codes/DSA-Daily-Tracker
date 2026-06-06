# PROBLEM NUMBER: 921
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# 921. Minimum Add to Make Parentheses Valid
# DIFFICULTY: MEDIUM

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Approach:
        # Traverse the string while keeping
        # track of unmatched opening brackets.
        #
        # For every '(' increase the count
        # of open brackets.
        #
        # For every ')' try to match it with
        # a previous '('.
        #
        # If no opening bracket is available,
        # we must add one, so increase the
        # required additions count.
        #
        # After traversal, any remaining
        # unmatched '(' also need matching
        # closing brackets.
        #
        # The answer is the total number of
        # additions required.

        open_count = 0
        additions = 0

        for ch in s:

            if ch == '(':

                open_count += 1

            else:

                if open_count > 0:
                    open_count -= 1
                else:
                    additions += 1

        return additions + open_count