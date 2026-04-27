# PROBLEM NUMBER:1021
# https://leetcode.com/problems/remove-outermost-parentheses/
# 1021. Remove Outermost Parentheses
# DIFFICULTY:EASY

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # We need to remove the outermost parentheses
        # from every primitive valid parentheses substring.
        #
        # Step 1: Use balance variable:
        #         • Tracks open parentheses count
        #
        # Step 2: Traverse each character
        #
        # Step 3: For '(':
        #         • If balance > 0:
        #             → not outermost, keep it
        #         • Then increase balance
        #
        # Step 4: For ')':
        #         • First decrease balance
        #         • If balance > 0:
        #             → not outermost, keep it
        #
        # Step 5: This skips:
        #         • First '(' of primitive
        #         • Last ')' of primitive
        #
        # Step 6: Join result and return

        res = []
        balance = 0

        for ch in s:
            if ch == '(':
                if balance > 0:
                    res.append(ch)
                balance += 1

            else:  # ')'
                balance -= 1
                if balance > 0:
                    res.append(ch)

        return "".join(res)