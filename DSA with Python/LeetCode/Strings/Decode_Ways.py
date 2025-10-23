# PROBLEM NUMBER: 91
# https://leetcode.com/problems/decode-ways/
# 91. Decode Ways
# DIFFICULTY: MEDIUM
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # This solution is an optimized space version of the Dynamic Programming approach for decoding ways.
        # 1. Handle edge cases: if the string is empty or starts with '0', return 0.
        # 2. Use two variables instead of a DP array:
        #    - `prev2` → number of ways to decode up to index i-2.
        #    - `prev1` → number of ways to decode up to index i-1.
        # 3. Iterate from the second character to the end of the string:
        #    - Initialize `curr = 0` for current index.
        #    - If `s[i]` is not '0', add `prev1` to `curr` (single-digit decoding is valid).
        #    - If the two-digit number `s[i-1:i+1]` is between 10 and 26, add `prev2` to `curr`.
        #    - Update `prev2, prev1 = prev1, curr` for next iteration.
        # 4. Return `prev1` as the total number of decoding ways.
        # Time Complexity: O(n) — single pass through the string.
        # Space Complexity: O(1) — only constant extra space used.
        if not s or s[0] == '0':
            return 0
        
        prev2 = 1
        prev1 = 1
        
        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0':
                curr += prev1
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                curr += prev2
            prev2, prev1 = prev1, curr
        
        return prev1