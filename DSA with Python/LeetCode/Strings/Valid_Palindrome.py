# PROBLEM NUMBER: 125
# https://leetcode.com/problems/valid-palindrome/
# 125. Valid Palindrome
# DIFFICULTY: Easy
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # APPROACH:
        # This solution checks whether a given string `s` is a palindrome considering only alphanumeric characters and ignoring cases.
        # 1. Use a list comprehension to filter out non-alphanumeric characters and convert all remaining characters to lowercase.
        # 2. Compare the filtered list with its reverse (`filtered[::-1]`).
        # 3. Return True if they are equal (palindrome), otherwise return False.
        # This approach ensures that spaces, punctuation, and letter cases do not affect the palindrome check, achieving O(n) time and space complexity.
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]