# PROBLEM NUMBER: 2108
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# 2108. Find First Palindromic String in the Array
# DIFFICULTY: EASY
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Approach:
        # Step 1: The goal is to find and return the first word in the list that is a palindrome.
        # Step 2: Traverse through the list of words one by one.
        # Step 3: For each word, check whether it is equal to its reversed version.
        # Step 4: The reversed version of the word can be obtained using Python slicing `[::-1]`.
        # Step 5: If the word is the same as its reversed version, it means the word is a palindrome.
        # Step 6: Immediately return that word because the problem asks for the first palindrome in the list.
        # Step 7: If the loop finishes and no palindrome word is found, return an empty string.
        for word in words:
            if word == word[::-1]:
                return word

        return ""