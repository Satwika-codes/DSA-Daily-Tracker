# PROBLEM NUMBER: 1234
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/
# 1234. Replace the Substring for Balanced String
# DIFFICULTY: MEDIUM
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # We need to find the minimum length substring that can be replaced
        # so that each character ('Q','W','E','R') appears exactly n/4 times.
        #
        # Step 1: Count frequency of each character in the string.
        #         • required = n // 4 (each character should appear this many times)
        #
        # Step 2: If already balanced (all counts == required):
        #         • Return 0
        #
        # Step 3: Use sliding window:
        #         • Idea → find the smallest substring such that
        #           removing it makes the remaining string balanced
        #
        # Step 4: Expand window using right pointer:
        #         • Decrease count of s[right]
        #           (since this character is now inside the window)
        #
        # Step 5: Check if remaining string is valid:
        #         • All characters outside window should have count <= required
        #
        # Step 6: While valid:
        #         • Update result with current window size
        #         • Shrink window from left
        #         • Restore count of s[left]
        #
        # Step 7: Continue until entire string is processed
        #
        # Step 8: Return minimum window size found

        n = len(s)
        count = Counter(s)
        required = n // 4

        # already balanced
        if all(count[c] == required for c in "QWER"):
            return 0

        res = n
        left = 0

        for right in range(n):
            count[s[right]] -= 1

            # check if remaining string is valid
            while left < n and all(count[c] <= required for c in "QWER"):
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1

        return res