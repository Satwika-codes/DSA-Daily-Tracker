# PROBLEM NUMBER :1160
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# 1160.Find words that can be formed by characters
# DIFFICULTY: EASY
class Solution(object):
    def countCharacters(self, words, chars):
        """
        APPROACH:
        - Count the frequency of each character in the given chars string.
        - For each word, count its character frequencies.
        - A word is valid if for every character, its frequency
          does not exceed what is available in chars.
        - If valid, add the length of the word to the total sum.
        """

        from collections import Counter

        char_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= char_count.get(c, 0) for c in word_count):
                total_length += len(word)

        return total_length
