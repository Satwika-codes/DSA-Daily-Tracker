#PROBLEM NUMBER: 242
#https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram
# DIFFICULTY: Easy
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # APPROACH:
        # This solution checks if two strings `s` and `t` are anagrams by comparing their character frequencies.
        # 1. If the lengths of `s` and `t` differ, return False immediately (anagrams must have equal length).
        # 2. Initialize a frequency array `count` of size 26 (for each lowercase English letter).
        # 3. Traverse string `s` and increment the count for each character.
        # 4. Traverse string `t` and decrement the count for each character:
        #    - If any count becomes zero before decrementing, it means `t` has an extra occurrence of that character — return False.
        # 5. If all counts balance out correctly, return True (both strings have identical character distributions).
        # This approach efficiently verifies anagrams without sorting.
        # Time Complexity: O(n) — single traversal of both strings.
        # Space Complexity: O(1) — fixed-size array of 26 for character counts.
        if len(s)!=len(t):
            return False
        count=[0]*26
        for char in s:
            count[ord(char)-ord('a')]+=1
        for char in t:
            if count [ord(char)-ord('a')]==0:
                return False
            count[ord(char)-ord('a')]-=1
        return True
        