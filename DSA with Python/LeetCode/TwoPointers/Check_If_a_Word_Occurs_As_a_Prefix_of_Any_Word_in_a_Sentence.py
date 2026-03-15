# PROBLEM NUMBER: 1455
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
# DIFFICULTY: EASY
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        # Approach:
        # Step 1: The goal is to find the position of the first word in the sentence where `searchWord` appears as a prefix.
        # Step 2: Split the given sentence into a list of individual words using the `split()` method, which separates words based on spaces.
        # Step 3: Traverse through the list of words using `enumerate()` so that both the index and the word can be accessed during iteration.
        # Step 4: For each word, check whether it starts with `searchWord` using the `startswith()` string method.
        # Step 5: If a word starts with `searchWord`, return its position in the sentence.
        # Step 6: Since the problem requires a 1-based index, return `i + 1` instead of the zero-based index `i`.
        # Step 7: If no word in the sentence starts with `searchWord`, return -1 to indicate that the prefix was not found.
        words = sentence.split()

        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1  # 1-based index

        return -1