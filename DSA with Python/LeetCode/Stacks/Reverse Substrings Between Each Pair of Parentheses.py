# PROBLEM NUMBER: 1190
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# 1190. Reverse Substrings Between Each Pair of Parentheses
# DIFFICULTY: MEDIUM

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Approach:
        # We use a stack to process nested
        # parentheses efficiently.
        #
        # Key Idea:
        # Whenever we encounter ')',
        # we reverse the substring inside
        # the most recent matching '('.
        #
        # Step 1:
        # Traverse each character in the string.
        #
        # Step 2:
        # If character is not ')':
        # • Push it onto the stack.
        #
        # Step 3:
        # If character is ')':
        #
        # • Pop characters until '(' is found.
        #
        # • Store popped characters in a temporary list.
        #
        # • Remove '(' from stack.
        #
        # • Push characters from temp back
        #   into the stack.
        #
        # Since characters are popped in reverse order,
        # pushing them back automatically gives
        # the required reversed substring.
        #
        # Step 4:
        # Continue until entire string
        # has been processed.
        #
        # Step 5:
        # Join all characters remaining
        # in the stack to form the answer.
        #
        # Parentheses are not included
        # in the final result.

        stack = []

        for ch in s:

            # Process closing parenthesis
            if ch == ')':

                temp = []

                # Collect characters inside parentheses
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())

                # Remove matching '('
                stack.pop()

                # Push reversed substring back
                for c in temp:
                    stack.append(c)

            # Push normal characters and '('
            else:
                stack.append(ch)

        return "".join(stack)