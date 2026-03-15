# PROBLEM NUMBER:1754
# https://leetcode.com/problems/largest-merge-of-two-strings/
# 1754. Largest Merge Of Two Strings
# DIFFICULTY: HARD
class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0
        merge = []

        while i < len(word1) and j < len(word2):
            # Compare remaining substrings
            if word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1

        # Append remaining part
        merge.append(word1[i:])
        merge.append(word2[j:])

        return "".join(merge)