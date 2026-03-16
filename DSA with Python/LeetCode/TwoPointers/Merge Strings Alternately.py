# PROBLEM NUMBER:1768
# https://leetcode.com/problems/merge-strings-alternately/
# 1768. Merge Strings Alternately
# DIFFICULTY: EASY
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Approach:
        # We need to merge two strings by taking characters alternately.
        
        # Step 1: Use two pointers:
        #         i → index for word1
        #         j → index for word2
        # Step 2: Create a list "res" to store characters of the merged string.
        # Step 3: While both strings still have characters:
        #         • Append word1[i]
        #         • Append word2[j]
        #         • Move both pointers forward
        # Step 4: After the loop, one string might still have characters left.
        #         Append the remaining substring from word1 or word2.
        # Step 5: Join the list to form the final string.

        i = 0
        j = 0
        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)