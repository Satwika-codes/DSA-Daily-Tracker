# PROBLEM NUMBER:1047
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# 1047. Remove All Adjacent Duplicates In String
# DIFFICULTY: EASY

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # We need to remove all adjacent duplicate characters.
        #
        # Step 1: Use a stack:
        #         • Helps track characters and remove duplicates instantly
        #
        # Step 2: Traverse the string:
        #         • For each character:
        #
        # Step 3: Check top of stack:
        #         • If stack not empty AND top == current character:
        #             → duplicate found
        #
        # Step 4: If duplicate:
        #         • Pop from stack (remove both)
        #
        # Step 5: Else:
        #         • Push current character into stack
        #
        # Step 6: Continue until end
        #
        # Step 7: Join stack to form final string

        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)