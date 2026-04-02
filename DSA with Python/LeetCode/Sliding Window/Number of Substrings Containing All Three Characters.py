# PROBLEM NUMBER: 1358
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# 1358.Number of Substrings Containing All Three Characters
# DIFFICULTY: MEDIUM
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # We need to count substrings that contain at least one 'a', 'b', and 'c'.
        #
        # Step 1: Use a hashmap (count) to track frequency of 'a', 'b', and 'c'
        #         in the current window.
        #
        # Step 2: Use sliding window with two pointers:
        #         • left → start of window
        #         • right → end of window
        #
        # Step 3: Expand window by moving right pointer:
        #         • Increase count of current character
        #
        # Step 4: When window becomes valid:
        #         • Condition → count['a'] > 0 AND count['b'] > 0 AND count['c'] > 0
        #
        # Step 5: Once valid:
        #         • All substrings starting from current left
        #           and ending from right to end are valid
        #         • So add (n - right) to result
        #
        # Step 6: Shrink window from left:
        #         • Decrease count of s[left]
        #         • Move left forward
        #
        # Step 7: Continue until entire string is processed
        #
        # Step 8: Return total count

        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        res = 0
        n = len(s)

        for right in range(n):
            count[s[right]] += 1

            # shrink when valid
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += (n - right)

                count[s[left]] -= 1
                left += 1

        return res