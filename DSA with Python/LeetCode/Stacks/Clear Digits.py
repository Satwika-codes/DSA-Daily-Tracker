# PROBLEM NUMBER: 3174
# https://leetcode.com/problems/clear-digits/
# 3174. Clear Digits
# DIFFICULTY: EASY

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Approach:
        # We remove the closest non-digit character
        # to the left whenever a digit appears.
        #
        # A stack helps us efficiently track
        # remaining characters.
        #
        # Step 1:
        # Traverse each character in the string.
        #
        # Step 2:
        # If character is a digit:
        # • Remove previous character
        # • Pop from stack
        #
        # Step 3:
        # If character is a letter:
        # • Push it into stack
        #
        # Step 4:
        # Remaining stack characters form
        # the final string.

        stack = []

        for ch in s:

            # If digit appears,
            # remove previous character
            if ch.isdigit():
                if stack:
                    stack.pop()

            # Store letters
            else:
                stack.append(ch)

        # Convert stack back to string
        return "".join(stack)