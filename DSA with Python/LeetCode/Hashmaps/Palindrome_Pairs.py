# PROBLEM NUMBER:-336
# https://leetcode.com/problems/palindrome-pairs/
# 336.Palindrome Pairs
# DIFFICULTY:-HARD
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        # Approach:
        # Use a hashmap to store each word with its index for quick lookup.
        # For every word, split it into two parts at every possible position.
        # Check if the left part is a palindrome and the reversed right part exists as a different word.
        # Check if the right part is a palindrome and the reversed left part exists as a different word.
        # Add valid index pairs to the result.
        # This avoids brute force comparison of all word pairs and works efficiently.

        def is_palindrome(word):
            return word == word[::-1]

        word_index = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]

                if is_palindrome(left):
                    rev_right = right[::-1]
                    if rev_right in word_index and word_index[rev_right] != i:
                        result.append([word_index[rev_right], i])

                if j != len(word) and is_palindrome(right):
                    rev_left = left[::-1]
                    if rev_left in word_index and word_index[rev_left] != i:
                        result.append([i, word_index[rev_left]])

        return result
