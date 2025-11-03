# PROBLEM NUMBER: 459
# https://leetcode.com/problems/repeated-substring-pattern/
# 459. Repeated Substring Pattern
# DIFFICULTY: EASY
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Approach:
        # If a string is made by repeating a substring, it will appear inside (s + s)[1:-1].
        # Example: "abab" → "abababab"[1:-1] = "bababa" → contains "abab" → True.
        # Time: O(n), Space: O(n)
        return s in (s + s)[1:-1]