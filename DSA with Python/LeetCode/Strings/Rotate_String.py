# PROBLEM NUMBER: 796
# https://leetcode.com/problems/rotate-string/
# 796. Rotate String
# DIFFICULTY: EASY
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Approach:
        # - Check if both strings have equal length (rotation is only possible if lengths match).
        # - Concatenate s with itself (s + s).  
        #   → Any rotation of s will appear as a substring in (s + s).
        # - Return True if goal exists in (s + s), otherwise False.
        # Time: O(n^2), Space: O(n)
        # Time: O(n^2), Space: O(n)
        return len(s) == len(goal) and goal in (s + s)
        