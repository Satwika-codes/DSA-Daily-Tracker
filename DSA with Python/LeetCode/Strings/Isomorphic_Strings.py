# PROBLEM NUMBER:205
# https://leetcode.com/problems/isomorphic-strings/
# 205.ISOMORPHIC STRINGS
# DIFFICULTY:Easy
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # APPROACH:  
        # This solution checks whether two strings `s` and `t` are *isomorphic* — meaning each character in `s` can be replaced 
        # to get `t` while maintaining the order and one-to-one mapping of characters.
        # 1. Create two dictionaries, `s1` and `t1`, to store the first occurrence index of each character in `s` and `t` respectively.  
        # 2. Iterate through both strings simultaneously:
        #    - If a character is seen for the first time, store its index in the respective dictionary.
        #    - Compare the first occurrence indices of the current characters from both strings.
        #    - If they differ, it means the mapping is inconsistent → return `False`.
        # 3. If the entire loop completes without mismatches, return `True`.
        # This method ensures both strings follow the same positional mapping pattern.
        # Time Complexity: O(n) — single pass through both strings.
        # Space Complexity: O(1) — at most 26–128 entries (bounded by character set size).
        s1 = {}
        t1 = {}
        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]] = i
            if t[i] not in t1:
                t1[t[i]] = i
            if s1[s[i]] != t1[t[i]]:
                return False
        return True
        