# PROBLEM NUMBER:424
# https://leetcode.com/problems/longest-repeating-character-replacement/
# 424. Longest Repeating Character Replacement
# DIFFICULTY:MEDIUM
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Approach:
        # We need to find the longest substring where we can replace
        # at most k characters to make all characters the same.
        #
        # Step 1: Use sliding window with two pointers (left, right)
        #
        # Step 2: Use hashmap (freq) to count characters in current window
        #
        # Step 3: Track max_freq:
        #         • maximum frequency of any character in current window
        #
        # Step 4: Expand window by moving right pointer:
        #         • Update frequency of s[right]
        #         • Update max_freq
        #
        # Step 5: Check if window is valid:
        #         • Window size - max_freq = number of characters to replace
        #         • If this exceeds k → window is invalid
        #
        # Step 6: If invalid:
        #         • Shrink window from left
        #         • Decrease freq of s[left]
        #         • Move left forward
        #
        # Step 7: If valid:
        #         • Update result with current window size
        #
        # Step 8: Return maximum length found

        freq = defaultdict(int)
        left = 0
        max_freq = 0
        res = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            # shrink if invalid
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res