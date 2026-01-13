# PROBLEM NUMBER :2781
# https://leetcode.com/problems/length-of-the-longest-valid-substring/
# 2781.Length of longest valid Substring
# DIFFICULTY :HARD
class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        """
        :type word: str
        :type forbidden: List[str]
        :rtype: int
        """
        # APPROACH:
        # 1. Store all forbidden strings in a set for O(1) lookup.
        # 2. Use a sliding window approach where we expand the right pointer
        #    and try to maintain the largest valid window.
        # 3. For each right index, check substrings ending at this index with
        #    lengths up to 10 (since forbidden word length ≤ 10).
        # 4. If any forbidden substring is found, move the left pointer to
        #    ensure the window becomes valid again.
        # 5. Track and update the maximum window size during the process.

        # Time Complexity:
        # - O(n * 10) ≈ O(n)

        # Space Complexity:
        # - O(len(forbidden))
    
        forbidden_set = set(forbidden)
        left = 0
        res = 0

        for right in range(len(word)):
            for l in range(1, 11):
                if right - l + 1 < left:
                    break
                if word[right - l + 1:right + 1] in forbidden_set:
                    left = right - l + 2
            res = max(res, right - left + 1)

        return res
