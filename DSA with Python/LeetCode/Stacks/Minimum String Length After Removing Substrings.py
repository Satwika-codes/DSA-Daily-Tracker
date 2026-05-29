# PROBLEM NUMBER: 2696
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
# 2696. Minimum String Length After Removing Substrings
# DIFFICULTY: EASY

class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Approach:
        # We repeatedly remove:
        # • "AB"
        # • "CD"
        #
        # Since removals can create new removable pairs,
        # we process the string using a stack.
        #
        # Step 1:
        # Traverse each character in the string.
        #
        # Step 2:
        # Check top of stack with current character:
        #
        # • If top = 'A' and current = 'B'
        #   → remove pair by popping stack
        #
        # • If top = 'C' and current = 'D'
        #   → remove pair by popping stack
        #
        # Step 3:
        # Otherwise push current character into stack.
        #
        # Step 4:
        # Remaining stack size is the minimum string length.

        stack = []

        for ch in s:

            # Check if removable pair exists
            if stack:

                # Remove "AB"
                if stack[-1] == 'A' and ch == 'B':
                    stack.pop()
                    continue

                # Remove "CD"
                if stack[-1] == 'C' and ch == 'D':
                    stack.pop()
                    continue

            # Push current character
            stack.append(ch)

        # Remaining characters
        return len(stack)