# PROBLEM NUMBER:1764
# https://leetcode.com/problems/longest-awesome-substring/
# 1764.Longest Awesome Substring
# DIFFICULTY: HARD
class Solution(object):
    def longestAwesome(self, s):
        """ 
        :type s:str 
        :rtype: int 
        """
        
        # APPROACH:
        # - An awesome substring is one where at most one digit appears an odd number of times.
        # - Use a bitmask of size 10 to track parity (even/odd) of digits 0–9.
        # - Traverse the string and update the mask by toggling the bit of the current digit.
        # - Store the earliest index at which each mask appears.
        # - A substring is awesome if:
        #    * The current mask has appeared before (all digits even), or
        #    * The current mask differs by exactly one bit from a previous mask
        #   (only one digit is odd).
        # - Track the maximum length of such valid substrings.
        

        mask = 0
        seen = {0: -1}
        max_len = 0

        for i, ch in enumerate(s):
            digit = ord(ch) - ord('0')
            mask ^= (1 << digit)

            if mask in seen:
                max_len = max(max_len, i - seen[mask])
            else:
                seen[mask] = i

            for d in range(10):
                temp = mask ^ (1 << d)
                if temp in seen:
                    max_len = max(max_len, i - seen[temp])

        return max_len
