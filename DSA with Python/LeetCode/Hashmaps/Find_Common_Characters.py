# PROBLEM NUMBER:1002
# 1002.Find Common Characters
# https://leetcode.com/problems/find-common-characters/
# DIFFICULTY: EASY
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Approach:
        # Take frequency count of characters from the first word
        # For every next word, take its frequency count
        # Update the main frequency by taking minimum count for each character
        # This ensures only common characters with correct repetitions remain
        # Finally, construct the result list using the final frequency map

        from collections import Counter

        freq = Counter(words[0])

        for word in words[1:]:
            freq &= Counter(word)

        result = []
        for ch in freq:
            result.extend([ch] * freq[ch])

        return result
