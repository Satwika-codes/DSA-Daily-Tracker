# PROBLEM NUMBER: 524
# 524.Longest Word in Dictionary through Deleting
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# DIFFICULTY: MEDIUM
class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        # Approach:
        # - For each word in the dictionary, check whether it is a subsequence of string s.
        # - A word is a subsequence if we can match all its characters in order while scanning s once.
        # - Among all valid subsequences:
        #     * Prefer the word with the maximum length.
        #     * If multiple words have the same length, choose the lexicographically smallest one.
        # - Keep updating the answer while iterating through the dictionary.
        def isSubsequence(word, s):
            i = j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return i == len(word)
        
        ans = ""
        
        for word in dictionary:
            if isSubsequence(word, s):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word
        
        return ans
