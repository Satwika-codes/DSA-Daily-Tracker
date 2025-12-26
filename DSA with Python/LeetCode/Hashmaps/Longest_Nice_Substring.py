# PROBLEM NUMBER:1763
# https://leetcode.com/problems/longest-nice-substring/
# 1763.Longest Nice Substring 
# DIFFICULTY:Longest Nice Substring 
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        # APPROACH:
        # - A substring is nice if for every character in it,
        #   both its uppercase and lowercase forms exist.
        # - Use divide and conquer:
            # * If a character violates the nice condition,
            #   it cannot be part of any nice substring.
            # * Split the string at that character and solve
            #  recursively for left and right parts.
        # - Return the longer nice substring from the recursive calls.
        def helper(sub):
            if len(sub) < 2:
                return ""

            chars = set(sub)
            for i, c in enumerate(sub):
                if c.swapcase() not in chars:
                    left = helper(sub[:i])
                    right = helper(sub[i + 1:])
                    return left if len(left) >= len(right) else right

            return sub

        return helper(s)
