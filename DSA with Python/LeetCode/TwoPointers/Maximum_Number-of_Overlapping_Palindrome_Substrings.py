# PROBLEM NUMBER: 2472
# https://leetcode.com/problems/maximum-number-of-overlapping-palindrome-substrings/
# 2472.Maximum Number of Overlapping Palindrome Substrings
# DIFFICULTY: HARD
class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """      
        # Approach:
        # 1. Precompute all palindromic substrings using DP.
        #    isPal[i][j] = True if s[i..j] is a palindrome.
        # 2. Use greedy DP:
        #    dp[i] = maximum number of valid palindromes using s[0:i]
        # 3. For each ending index i, try all palindromes of length >= k
        #    that end at i and update dp.

        # Key idea:
        # - Always take the earliest-ending palindrome (greedy works).
        # - DP ensures non-overlapping substrings.

        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)
        

        n = len(s)
        isPal = [[False] * n for _ in range(n)]

        for i in range(n):
            isPal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or isPal[i + 1][j - 1]:
                        isPal[i][j] = True

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]  
            for j in range(i - k, -1, -1):
                if isPal[j][i - 1] and i - j >= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]
