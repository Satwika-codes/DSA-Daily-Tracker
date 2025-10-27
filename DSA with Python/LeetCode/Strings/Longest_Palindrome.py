# PROBLEM NUMBER: 409
# https://leetcode.com/problems/longest-palindrome/
# 409. Longest Palindrome
# DIFFICULTY: EASY
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # 1. Count the frequency of each character in the string.
        # 2. For every character:
        #       - If its frequency is even, we can use all occurrences.
        #       - If its frequency is odd, we can use (frequency - 1) 
        #         and mark that one odd character exists.
        # 3. After processing all characters:
        #       - If at least one character had an odd frequency, we can 
        #         place exactly one odd character in the middle of the palindrome.
        # 4. Return the total calculated length.
        # Complexity:
        #    - Time:  O(n)
        #    - Space: O(1)   (since character set is constant)
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        length = 0
        odd = False
        for val in freq.values():
            if val % 2 == 0:
                length += val
            else:
                length += val - 1
                odd = True
        return length + 1 if odd else length
        