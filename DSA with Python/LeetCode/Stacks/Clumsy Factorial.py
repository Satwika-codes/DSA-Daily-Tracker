# PROBLEM NUMBER: 1006
# https://leetcode.com/problems/clumsy-factorial/
# 1006. Clumsy Factorial
# DIFFICULTY: MEDIUM

class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Approach:
        # Clumsy factorial applies operators
        # in the repeating order:
        #
        # • *
        # • /
        # • +
        # • -
        #
        # Example:
        #
        # n * (n-1) / (n-2) + (n-3)
        # - (n-4) * (n-5) / (n-6)
        # + ...
        #
        # We use a stack to naturally handle
        # operator precedence.
        #
        # Step 1:
        # Push the first number (n)
        # into the stack.
        #
        # Step 2:
        # Process remaining numbers
        # from n-1 down to 1.
        #
        # Step 3:
        # Apply operations cyclically:
        #
        # op % 4 == 0 → Multiplication
        # op % 4 == 1 → Division
        # op % 4 == 2 → Addition
        # op % 4 == 3 → Subtraction
        #
        # Step 4:
        # For '*' and '/':
        #
        # • Modify stack top directly
        #   because they have higher precedence.
        #
        # Step 5:
        # For '+' and '-':
        #
        # • Push positive or negative values
        #   into the stack.
        #
        # Step 6:
        # Sum all values in stack
        # to obtain the final result.

        stack = [n]

        n -= 1

        op = 0

        while n > 0:

            # Multiplication
            if op % 4 == 0:

                stack[-1] *= n

            # Division
            elif op % 4 == 1:

                stack[-1] = int(float(stack[-1]) / n)

            # Addition
            elif op % 4 == 2:

                stack.append(n)

            # Subtraction
            else:

                stack.append(-n)

            op += 1

            n -= 1

        return sum(stack)