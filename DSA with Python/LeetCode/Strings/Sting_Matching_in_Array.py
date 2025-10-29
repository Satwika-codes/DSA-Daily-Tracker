# PROBLEM NUMBER: 1408
# https://leetcode.com/problems/string-matching-in-an-array/
# 1408. String Matching in an Array
# DIFFICULTY: EASY
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Approach:
        # The task is to find all strings in the list `words` that are 
        # substrings of another word in the same list. 
        # Idea:
        # We simply compare every pair of words (i, j) where i ≠ j.
        # For each word[i], check if it exists as a substring in word[j].
        # If yes, we add it to the result and break (since we only need 
        # to know if it’s present in any one other word).
        # Complexity:
        #   - Time:  O(n² * m)  
        #       (for each pair, substring check takes up to O(m))
        #   - Space: O(1) — only result list used.
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res