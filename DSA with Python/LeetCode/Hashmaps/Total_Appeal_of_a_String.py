# PROBLEM NUMBER: 2262
# https://leetcode.com/problems/total-appeal-of-a-string/
# 2262.Total Appeal of a String
# DIFFICULTY: HARD
class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # The appeal of a substring is the number of distinct characters in it.

        # Instead of enumerating all substrings, we calculate the contribution
        # of each character independently.

        # For each character, we track its last occurrence index.
        # At position i, the number of substrings ending at i where this
        # character contributes to the appeal is (i - last_index).

        # We maintain a running sum of appeal values for substrings ending
        # at each index and accumulate it into the final answer.

        # This allows us to compute the total appeal in O(n) time.
        

        last = {}
        curr = 0
        total = 0

        for i, ch in enumerate(s):
            curr += i - last.get(ch, -1)
            last[ch] = i
            total += curr

        return total
