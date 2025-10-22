# PROBLEM NUMBER: 290
# https://leetcode.com/problems/word-pattern/
# 290. Word Pattern
# DIFFICULTY: EASY
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # 💡 Approach:
        # 1. Split the string `s` into individual words using split().
        # 2. If the number of pattern characters and words are not equal, return False.
        # 3. Use two hash maps (dictionaries):
        #       - char_to_word → to map pattern characters to words.
        #       - word_to_char → to map words back to pattern characters.
        # 4. Traverse both pattern and words together using zip():
        #       - If a character is already mapped to a different word → return False.
        #       - If a word is already mapped to a different character → return False.
        #       - Otherwise, store the new mapping in both dictionaries.
        # 5. After checking all pairs, return True (pattern follows the word mapping correctly).

        words = s.split()
        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, w in zip(pattern, words):
            if ch in char_to_word and char_to_word[ch] != w:
                return False
            if w in word_to_char and word_to_char[w] != ch:
                return False
            char_to_word[ch] = w
            word_to_char[w] = ch

        return True