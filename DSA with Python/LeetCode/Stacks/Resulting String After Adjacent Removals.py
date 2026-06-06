# PROBLEM NUMBER: 3467
# https://leetcode.com/problems/transform-array-by-removing-adjacent-almost-equal-characters/
# 3467. Resulting String After Adjacent Removals
# DIFFICULTY: MEDIUM

class Solution(object):
    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Approach:
        # We use a stack to simulate the
        # removal process efficiently.
        #
        # Traverse the string character by
        # character and compare the current
        # character with the stack top.
        #
        # If the two characters are consecutive
        # in the alphabet (difference = 1) or
        # circularly consecutive ('a' and 'z'),
        # remove the previous character by
        # popping the stack.
        #
        # Otherwise, push the current character.
        #
        # The remaining characters in the stack
        # form the final resulting string.

        stack = []

        for ch in s:

            if stack:

                a = stack[-1]

                diff = abs(ord(a) - ord(ch))

                # Consecutive or circular consecutive
                if diff == 1 or diff == 25:
                    stack.pop()
                    continue

            stack.append(ch)

        return "".join(stack)