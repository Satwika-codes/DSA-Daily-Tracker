# PROBLEM NUMBER: 1424
# https://leetcode.com/problems/subsequence-with-minimum-score
# 1424. Subsequence With Minimum Score
# DIFFICULTY: HARD
class Solution(object):
    def minimumScore(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Approach:
        # - Precompute how much of t can be matched as a subsequence in s
        #   from the left (prefix matches).
        # - Precompute how much of t can be matched as a subsequence in s
        #   from the right (suffix matches).
        # - Try removing a substring t[i:j], such that:
        #       prefix t[0:i] + suffix t[j:] is a subsequence of s.
        # - Minimize (j - i).

        # Time Complexity: O(n + m)
        # Space Complexity: O(m)
        

        n, m = len(s), len(t)

        # left[i] = earliest index in s after matching t[0:i]
        left = [-1] * (m + 1)
        left[0] = 0

        i = 0
        for j in range(m):
            while i < n and s[i] != t[j]:
                i += 1
            if i == n:
                break
            i += 1
            left[j + 1] = i

        # If entire t is subsequence of s
        if left[m] != -1:
            return 0

        # right[i] = latest index in s before matching t[i:m]
        right = [-1] * (m + 1)
        right[m] = n

        i = n - 1
        for j in range(m - 1, -1, -1):
            while i >= 0 and s[i] != t[j]:
                i -= 1
            if i < 0:
                break
            right[j] = i
            i -= 1

        ans = m
        j = 0

        # Try removing t[i:j]
        for i in range(m + 1):
            if left[i] == -1:
                break
            while j < m and (right[j] == -1 or right[j] < left[i]):
                j += 1
            ans = min(ans, j - i)

        return ans
