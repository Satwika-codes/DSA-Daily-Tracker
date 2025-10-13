# PROBLEM NUMBER:5
# https://leetcode.com/problems/longest-palindromic-substring/
# 5.Longest Palindromic substring
# DIFFICULTY:Medium
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # APPROACH:
        # This solution finds the longest palindromic substring in a given string `s`
        # using the "Expand Around Center" technique
        # 1. Initialize `res` (to store the longest palindrome) and `res_len` (to store its length).
        # 2. Iterate through each index `i` in `s`:
        #    - Treat `i` as the center of a potential palindrome.
        #    - Expand outward in both directions (`l` and `r`) while `s[l] == s[r]`.
        #    - Update `res` and `res_len` whenever a longer palindrome is found.
        # 3. Perform the expansion twice for each `i`:
        #    - Once for odd-length palindromes (center at one character).
        #    - Once for even-length palindromes (center between two characters).
        # 4. After checking all possible centers, return `res` — the longest palindrome found.
        # This approach efficiently checks all palindromic centers in O(n²) time
        # and uses O(1) extra space.
        res = ""
        res_len = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return res
        