# PROBLEM NUMBER: 387
# https://leetcode.com/problems/first-unique-character-in-a-string/
# 387. First Unique Character in a String
# DIFFICULTY: EASY
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # This solution finds the index of the first non-repeating character in a string using a **hash map**.
        # 1. Initialize a dictionary `count` to store the frequency of each character in `s`.
        # 2. Iterate through the string and update the count for each character.
        # 3. Iterate through the string again:
        #    - If the count of a character is 1, return its index (first unique character).
        # 4. If no unique character is found, return -1.
        # Time Complexity: O(n) — two passes over the string.
        # Space Complexity: O(n) — for storing character counts.
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
        