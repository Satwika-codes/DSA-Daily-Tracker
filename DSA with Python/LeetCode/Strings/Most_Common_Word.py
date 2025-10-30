# PROBLEM NUMBER: 819
# https://leetcode.com/problems/most-common-word/
# 819. Most Common Word
# DIFFICULTY: EASY
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Approach:
        # The task is to find the most common (non-banned) word in a paragraph.
        # 1. Convert the entire paragraph to lowercase for case-insensitive comparison.
        # 2. Parse each character:
        #       - Build words from alphabetic characters.
        #       - When encountering a non-alphabetic character, finalize the current word.
        # 3. Add all parsed words into a list `words`.
        # 4. Create a `set` from the banned words for O(1) lookup.
        # 5. Count frequencies of all non-banned words using a dictionary `freq`.
        # 6. Track the word with the highest frequency.
        # 7. Return the most frequent non-banned word.
        paragraph = paragraph.lower()
        word = ""
        words = []
        for ch in paragraph:
            if ch.isalpha():
                word += ch
            else:
                if word != "":
                    words.append(word)
                    word = ""
        if word != "":
            words.append(word)
        banned_set = set(banned)
        freq = {}
        for w in words:
            if w not in banned_set:
                if w in freq:
                    freq[w] += 1
                else:
                    freq[w] = 1
        max_count = 0
        result = ""
        for w in freq:
            if freq[w] > max_count:
                max_count = freq[w]
                result = w
        return result
