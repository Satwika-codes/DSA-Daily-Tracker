# PROBLEM NUMBER: 3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3.Longest substring without repeating characters
# DIFFICULTY:MEDIUM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # APPROACH:
        # This solution finds the length of the longest substring without repeating characters using the sliding window technique.
        # 1. Use a dictionary `char_index` to store the most recent index of each character encountered.
        # 2. Maintain two pointers:
        #    - `left`: marks the start of the current substring window.
        #    - `right`: iterates over the string characters.
        # 3. For each character `s[right]`:
        #    - If it already exists in `char_index` and its stored index is ≥ `left`, 
        #      move the `left` pointer to one position right of the previous occurrence to avoid repetition.
        # 4. Update `char_index[s[right]]` with the current index `right`.
        # 5. Calculate the window length as `(right - left + 1)` and track the maximum in `max_len`.
        # 6. Finally, return `max_len` as the length of the longest substring without duplicates.
        # Time Complexity: O(n) — each character is processed at most twice (once by `right`, once by `left`).
        # Space Complexity: O(min(n, m)) — where m is the character set size (for storing indices in the dictionary).
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
        