# PROBLEM NUMBER: 28
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # APPROACH:
        # This solution finds the first occurrence of the substring `needle` in the string `haystack`.
        # 1. If `needle` is an empty string, return 0 as per the problem definition.
        # 2. Use Python’s built-in `str.find()` method, which returns:
        #    - The index of the first occurrence of `needle` in `haystack`, if found.
        #    - -1 if `needle` is not found.
        # This approach leverages an efficient built-in substring search implementation, typically based on advanced algorithms like 
        # Boyer-Moore or similar, providing optimal performance with clean, concise code.
        if needle == "":
            return 0
        return haystack.find(needle)