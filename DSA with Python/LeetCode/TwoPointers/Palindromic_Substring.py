# PROBLEM NUMBER: 647
# https://leetcode.com/problems/palindromic-substrings/
# 647. Palindromic Substrings
# DIFFICULTY: MEDIUM
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # - Every palindrome is centered at either:
        #     1) a single character (odd length)
        #     2) between two characters (even length)
        # - For each possible center, expand outward while characters match.
        # - Count all valid expansions.

        # This avoids DP and runs efficiently.

        # Time Complexity:  O(n^2)
        # Space Complexity: O(1)
        

        n = len(s)
        ans = 0

        def expand(l, r):
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt

        for i in range(n):
            ans += expand(i, i)       # odd-length palindromes
            ans += expand(i, i + 1)   # even-length palindromes

        return ans
