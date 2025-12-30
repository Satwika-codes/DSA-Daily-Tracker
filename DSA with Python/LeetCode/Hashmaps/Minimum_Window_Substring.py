# PROBLEM NUMBER:76
# https://leetcode.com/problems/minimum-Window-Substing
# 76.Minimum Window substring
# DIFFICULTY: HARD
class Solution(object):
    def minWindow(self, s, t):
        """
        APPROACH:
        - Use the sliding window technique to find the minimum window in `s`
          that contains all characters of `t`.
        - Maintain a frequency map for characters in `t` and a counter
          for how many required characters are still missing.
        - Expand the right pointer to include characters until all
          requirements are met.
        - Shrink the left pointer to minimize the window while
          keeping it valid.
        - Track and return the smallest valid window found.
        """

        from collections import Counter

        if not s or not t:
            return ""

        t_count = Counter(t)
        required = len(t)
        left = 0
        min_len = float('inf')
        start = 0

        for right, char in enumerate(s):
            if char in t_count:
                if t_count[char] > 0:
                    required -= 1
                t_count[char] -= 1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                if left_char in t_count:
                    t_count[left_char] += 1
                    if t_count[left_char] > 0:
                        required += 1
                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]
