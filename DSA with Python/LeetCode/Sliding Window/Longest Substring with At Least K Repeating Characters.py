# PROBLEM NUMBER: 395
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# 395. Longest Substring with At Least K Repeating Characters
# DIFFICULTY: HARD
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # Approach:
        # We need the longest substring where every character appears at least k times.
        #
        # Key Idea:
        # Try all possible counts of unique characters (1 to 26),
        # and use sliding window to enforce that condition.
        #
        # Step 1: Iterate target_unique from 1 to 26.
        #
        # Step 2: Use sliding window with:
        #         • freq array of size 26
        #         • left, right pointers
        #
        # Step 3: Maintain:
        #         • unique → number of unique characters in window
        #         • countAtLeastK → number of chars with freq ≥ k
        #
        # Step 4: Expand window (move right):
        #         • Update frequency
        #         • If new char → increase unique
        #         • If freq becomes k → increase countAtLeastK
        #
        # Step 5: Shrink window if unique > target_unique:
        #         • Decrease frequency
        #         • If freq becomes k-1 → decrease countAtLeastK
        #         • If freq becomes 0 → decrease unique
        #
        # Step 6: Valid condition:
        #         • unique == target_unique
        #         • unique == countAtLeastK
        #
        # Step 7: Update max_len if valid.
        #
        # Step 8: Return maximum length found.

        max_len = 0

        for target_unique in range(1, 27):
            freq = [0] * 26
            left = 0
            right = 0

            unique = 0
            countAtLeastK = 0

            while right < len(s):
                # expand window
                idx = ord(s[right]) - ord('a')
                if freq[idx] == 0:
                    unique += 1
                freq[idx] += 1
                if freq[idx] == k:
                    countAtLeastK += 1

                right += 1

                # shrink window
                while unique > target_unique:
                    idx = ord(s[left]) - ord('a')
                    if freq[idx] == k:
                        countAtLeastK -= 1
                    freq[idx] -= 1
                    if freq[idx] == 0:
                        unique -= 1
                    left += 1

                # check valid
                if unique == target_unique and unique == countAtLeastK:
                    max_len = max(max_len, right - left)

        return max_len