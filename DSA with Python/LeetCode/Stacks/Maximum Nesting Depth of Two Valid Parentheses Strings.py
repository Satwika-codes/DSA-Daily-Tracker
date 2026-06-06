# PROBLEM NUMBER: 1111
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
# DIFFICULTY: MEDIUM

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """

        # Approach:
        # We split the parentheses into
        # two groups such that the maximum
        # nesting depth of both groups is
        # minimized.
        #
        # Track the current nesting depth
        # while traversing the string.
        #
        # For every opening bracket,
        # increase the depth and assign it
        # based on the parity of the depth.
        #
        # For every closing bracket,
        # assign it using the current depth
        # before decreasing the depth.
        #
        # This alternates nested parentheses
        # between the two groups, balancing
        # their depths as evenly as possible.

        depth = 0
        ans = []

        for ch in seq:

            if ch == '(':

                depth += 1
                ans.append(depth % 2)

            else:

                ans.append(depth % 2)
                depth -= 1

        return ans