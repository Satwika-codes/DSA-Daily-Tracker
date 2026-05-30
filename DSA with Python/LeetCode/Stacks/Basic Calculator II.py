# PROBLEM NUMBER: 227
# https://leetcode.com/problems/basic-calculator-ii/
# 227. Basic Calculator II
# DIFFICULTY: MEDIUM

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Approach:
        # We evaluate the expression using a stack
        # while handling operator precedence.
        #
        # Operators:
        # • +
        # • -
        # • *
        # • /
        #
        # Key Insight:
        # • Addition and subtraction can be postponed
        #   by storing numbers in the stack.
        #
        # • Multiplication and division must be
        #   performed immediately because they have
        #   higher precedence.
        #
        # Step 1:
        # Maintain:
        #
        # • stack → stores processed numbers
        # • num   → current number being formed
        # • op    → previous operator
        #
        # Step 2:
        # Traverse the string character by character.
        #
        # Step 3:
        # If current character is a digit:
        # • Build the complete number.
        #
        # Example:
        # "123"
        # → 1 → 12 → 123
        #
        # Step 4:
        # When an operator is encountered,
        # process the previous operator.
        #
        # • '+' → push number
        # • '-' → push negative number
        # • '*' → multiply stack top
        # • '/' → divide stack top by number
        #
        # Step 5:
        # Update operator and reset number.
        #
        # Step 6:
        # Append an extra '+' at the end
        # so the final number gets processed.
        #
        # Step 7:
        # Sum all values in stack
        # to get the final answer.

        stack = []
        num = 0
        op = '+'

        # Sentinel operator
        s += '+'

        for ch in s:

            # Build multi-digit number
            if ch.isdigit():
                num = num * 10 + int(ch)

            # Ignore spaces
            elif ch == ' ':
                continue

            else:

                # Addition
                if op == '+':
                    stack.append(num)

                # Subtraction
                elif op == '-':
                    stack.append(-num)

                # Multiplication
                elif op == '*':
                    stack[-1] *= num

                # Division
                elif op == '/':
                    stack[-1] = int(float(stack[-1]) / num)

                # Update operator
                op = ch

                # Reset current number
                num = 0

        return sum(stack)