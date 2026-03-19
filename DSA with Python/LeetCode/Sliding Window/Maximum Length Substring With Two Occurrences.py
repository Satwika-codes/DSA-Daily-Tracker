# PROBLEM NUMBER: 3090
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences-of-character/
# Maximum Length Substring With Two Occurrences of Character
# DIFFICULTY: EASY
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Approach:
        # We need to find the maximum length substring such that
        # no character appears more than 2 times.
        #
        # Step 1: Use sliding window with two pointers (left, right).
        #
        # Step 2: Maintain a frequency map (dictionary) to track
        #         the count of each character in the current window.
        #
        # Step 3: Expand the window by moving 'right' and updating
        #         the frequency of s[right].
        #
        # Step 4: If the frequency of the current character exceeds 2,
        #         shrink the window from the left until it becomes valid.
        #
        # Step 5: While shrinking, decrease the frequency of s[left]
        #         and move left pointer forward.
        #
        # Step 6: After ensuring the window is valid, calculate
        #         the current window length (right - left + 1)
        #         and update max_len.
        #
        # Step 7: Continue until the entire string is processed.
        #
        # Step 8: Return the maximum length found.

        left = 0
        freq = {}
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            # shrink window if any char appears more than 2 times
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len