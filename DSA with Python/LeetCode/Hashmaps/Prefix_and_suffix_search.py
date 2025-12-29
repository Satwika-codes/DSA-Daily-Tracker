#PROBLEM NUMBER :745
# https://leetcode.com/problems/prefix-and-suffix-search/
# 745.Prefix and suffix
# DIFFICULTY:HARD
class WordFilter(object):

    def __init__(self, words):
        """
        APPROACH:
        - The task is to find the word with the highest index that matches
          both a given prefix and suffix.
        - Precompute all possible (prefix, suffix) combinations for each word.
        - Store them in a hashmap with the word’s index as the value.
        - If multiple words map to the same (prefix, suffix), keep the largest index.
        - This allows each query to be answered in O(1) time.
        """

        self.lookup = {}

        for index, word in enumerate(words):
            length = len(word)
            for i in range(length + 1):
                pref = word[:i]
                for j in range(length + 1):
                    suff = word[j:]
                    self.lookup[(pref, suff)] = index

    def f(self, pref, suff):
        """
        APPROACH:
        - Look up the (prefix, suffix) pair in the precomputed hashmap.
        - Return the stored index if found, otherwise return -1.
        """

        return self.lookup.get((pref, suff), -1)
