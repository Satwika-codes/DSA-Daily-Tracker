# PROBLEM NUMBER: 1961
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
# 1961.Check If String Is a Prefix of Array
# DIFFICULTY: EASY
class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        # Approach:
        # Step 1: We need to check whether string s can be formed by concatenating
        #         the first k strings of the list words (k >= 1).
        # Step 2: Start with an empty string called "current".
        # Step 3: Traverse through each word in the words list.
        # Step 4: Append the word to current.
        # Step 5: After each append:
        #         • If current == s → we successfully formed s → return True.
        #         • If current becomes longer than s → it can never match → return False.
        # Step 6: If we finish the loop and never match s exactly → return False.

        current = ""

        for word in words:
            current += word

            if current == s:
                return True

            if len(current) > len(s):
                return False

        return False