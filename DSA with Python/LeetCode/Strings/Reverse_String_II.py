# PROBLEM NUMBER:541
# https://leetcode.com/problems/reverse-string-ii/
# 541. Reverse String II
# DIFFICULTY: EASY
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #  Approach:
        # This problem involves reversing every first `k` characters for each block of `2k` characters in the string.
        # 1. Convert the string `s` into a list since strings are immutable in Python.
        # 2. Iterate through the list in steps of `2k`:
        #    - For each segment, reverse the first `k` characters (`s[i:i + k]`).
        # 3. After processing all segments, join the list back into a string and return it.
        # Time Complexity: O(n) — each character is processed at most once.
        # Space Complexity: O(n) — due to list conversion.
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return ''.join(s)