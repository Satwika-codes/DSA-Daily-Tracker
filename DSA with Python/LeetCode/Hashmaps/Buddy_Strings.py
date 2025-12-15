# PROBLEM NUMBER: 859
# https://leetcode.com/problems/buddy-strings/
# Buddy Strings
# DIFFICULTY: EASY
class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        # Approach:
        # - If lengths differ, swapping cannot make strings equal.
        # - If strings are already equal, check if any character appears
        #   more than once (so a swap doesn't change the string).
        # - Otherwise, record indices where characters differ.
        # - Exactly two mismatches must exist.
        # - Swapping those two characters in 's' should make it equal to 'goal'.

        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        if len(diff) != 2:
            return False

        i, j = diff
        return s[i] == goal[j] and s[j] == goal[i]
