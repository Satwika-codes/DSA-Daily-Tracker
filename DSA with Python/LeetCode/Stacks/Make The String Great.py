# PROBLEM NUMBER: 1544
# https://leetcode.com/problems/make-the-string-great/
# 1544. Make The String Great
# DIFFICULTY: EASY
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # We need to remove adjacent characters where:
        # • Same letter but different case (e.g., 'a' & 'A')
        #
        # Step 1: Use a stack:
        #         • Helps track characters and remove invalid pairs
        #
        # Step 2: Traverse the string:
        #         • For each character:
        #
        # Step 3: Check top of stack:
        #         • If stack not empty AND
        #           current char differs by 32 in ASCII:
        #           → they are same letter, opposite case
        #
        # Step 4: If condition satisfied:
        #         • Pop from stack (remove pair)
        #
        # Step 5: Else:
        #         • Push current character into stack
        #
        # Step 6: Continue until end of string
        #
        # Step 7: Join stack to form final string

        stack = []

        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)