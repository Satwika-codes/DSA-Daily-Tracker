# PROBLEM NUMBER: 680
# https://leetcode.com/problems/valid-palindrome-ii/
# 680. Valid Palindrome II
# DIFFICULTY: EASY
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Approach:
        # 1. The goal is to determine if the string `s` can become a palindrome
        #    by deleting at most one character.
        # 2. Use two pointers (`i` at start, `j` at end):
        #       - Move inward while characters match.
        #       - When a mismatch occurs:
        #           → Try skipping either the left character (`i`) or
        #             the right character (`j`) once.
        #           → Check if either resulting substring is a palindrome.
        # 3. Helper Function: `is_palindrome(i, j)`
        #       - Checks if substring `s[i:j+1]` is a palindrome by comparing
        #         characters from both ends.
        # 4. If no mismatch or one valid skip makes it a palindrome → return True.
        #    Otherwise → return False.
        # Time Complexity: O(n)  # Single pass with possible one extra check
        # Space Complexity: O(1)
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True