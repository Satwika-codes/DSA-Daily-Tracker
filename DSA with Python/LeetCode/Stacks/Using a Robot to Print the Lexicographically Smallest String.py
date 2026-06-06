# PROBLEM NUMBER: 2434
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
# 2434. Using a Robot to Print the Lexicographically Smallest String
# DIFFICULTY: MEDIUM

class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Approach:
        # We want to build the lexicographically
        # smallest possible string using the
        # robot operations.
        #
        # First, compute the minimum character
        # that appears from every position to
        # the end of the string.
        #
        # Then process characters from left
        # to right, pushing them into a stack.
        #
        # If the stack top is smaller than or
        # equal to the minimum character that
        # can still appear later, it is safe
        # to output it immediately.
        #
        # Keep popping such characters into
        # the answer and finally return the
        # constructed string.

        n = len(s)

        suffix_min = [''] * n
        suffix_min[-1] = s[-1]

        for i in range(n - 2, -1, -1):

            suffix_min[i] = min(
                s[i],
                suffix_min[i + 1]
            )

        stack = []
        ans = []

        for i in range(n):

            stack.append(s[i])

            while (
                stack and
                (
                    i == n - 1 or
                    stack[-1] <= suffix_min[i + 1]
                )
            ):

                ans.append(stack.pop())

        return "".join(ans)