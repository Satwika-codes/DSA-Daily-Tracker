# PROBLEM NUMBER: 1332
# https://leetcode.com/problems/remove-palindromic-subsequences/
# 1332. Remove Palindromic Subsequences
# DIFFICULTY: Easy
class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # Step 1: The problem allows removing a subsequence that is a palindrome.
        # Step 2: The string only contains two characters: 'a' and 'b'.
        # Step 3: If the entire string itself is a palindrome, we can remove it in one step.
        # Step 4: If it is not a palindrome, we can remove all 'a' characters in one step
        #         and all 'b' characters in another step.
        # Step 5: Therefore the answer can only be:
        #         - 0 → if the string is empty
        #         - 1 → if the string itself is a palindrome
        #         - 2 → otherwise
        if not s:
            return 0

        # If s is palindrome
        if s == s[::-1]:
            return 1

        return 2