# PROBLEM NUMBER: 709
# https://leetcode.com/problems/to-lower-case/
# 709. To Lower Case
# DIFFICULTY: EASY
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # This solution converts all uppercase letters in the input string `s` to lowercase.
        # 1. Use Python's built-in `str.lower()` method which returns a copy of the string
        #    with all uppercase characters converted to lowercase.
        # 2. Return the resulting lowercase string.
        # Time Complexity: O(n) — where n is the length of the string.
        # Space Complexity: O(n) — for the new s
        return s.lower()