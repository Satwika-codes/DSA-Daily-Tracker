# PROBLEM NUMBER:1614
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# 1614. Maximum Nesting Depth of the Parentheses
# 
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach:
        # We need maximum nesting depth of parentheses.
        #
        # Step 1: Use depth variable:
        #         • Tracks current nesting level
        #
        # Step 2: Use max_depth:
        #         • Stores deepest nesting seen so far
        #
        # Step 3: Traverse each character
        #
        # Step 4: If '(':
        #         • Increase current depth
        #         • Update maximum depth
        #
        # Step 5: If ')':
        #         • Decrease current depth
        #
        # Step 6: Ignore digits/operators
        #         • They do not affect nesting
        #
        # Step 7: Return max_depth

        depth = 0
        max_depth = 0

        for ch in s:
            if ch == '(':
                depth += 1
                max_depth = max(max_depth, depth)

            elif ch == ')':
                depth -= 1

        return max_depth