# PROBLEM NUMBER: 150
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# 150. Evaluate Reverse Polish Notation
# DIFFICULTY: MEDIUM

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        # Approach:
        # We evaluate the Reverse Polish Notation (RPN)
        # expression using a stack.
        #
        # In RPN:
        # • Operators come after operands.
        #
        # Example:
        # ["2", "1", "+", "3", "*"]
        #
        # Evaluation:
        # (2 + 1) * 3 = 9
        #
        # Step 1:
        # Create an empty stack.
        #
        # Step 2:
        # Traverse each token.
        #
        # Step 3:
        # If token is a number:
        # • Convert to integer
        # • Push into stack
        #
        # Step 4:
        # If token is an operator:
        # • Pop two numbers
        # • First popped = second operand (b)
        # • Second popped = first operand (a)
        #
        # Order matters for:
        # • subtraction
        # • division
        #
        # Step 5:
        # Perform operation:
        #
        # • '+' → a + b
        # • '-' → a - b
        # • '*' → a * b
        # • '/' → a / b
        #
        # Step 6:
        # Push result back into stack.
        #
        # Step 7:
        # Final answer will be the
        # only element left in stack.

        stack = []

        for token in tokens:

            # Number
            if token not in "+-*/":

                stack.append(int(token))

            # Operator
            else:

                b = stack.pop()
                a = stack.pop()

                # Addition
                if token == '+':
                    stack.append(a + b)

                # Subtraction
                elif token == '-':
                    stack.append(a - b)

                # Multiplication
                elif token == '*':
                    stack.append(a * b)

                # Division
                else:
                    stack.append(int(float(a) / b))

        return stack[-1]