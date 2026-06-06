# PROBLEM NUMBER: 1106
# https://leetcode.com/problems/parsing-a-boolean-expression/
# 1106. Parsing A Boolean Expression
# DIFFICULTY: HARD

class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """

        # Approach:
        # We use a stack to evaluate the
        # boolean expression from inside
        # out whenever a closing bracket
        # is encountered.
        #
        # Push operators, operands, and
        # opening brackets onto the stack.
        #
        # When ')' is found, collect all
        # values until the matching '('.
        #
        # Then apply the corresponding
        # operator ('!', '&', or '|')
        # and push the result back onto
        # the stack.
        #
        # After processing the entire
        # expression, the stack contains
        # the final boolean result.

        stack = []

        for ch in expression:

            if ch == ',':
                continue

            elif ch != ')':
                stack.append(ch)

            else:

                vals = set()

                while stack[-1] != '(':
                    vals.add(stack.pop())

                stack.pop()  # remove '('

                op = stack.pop()

                if op == '!':

                    stack.append(
                        't' if 'f' in vals else 'f'
                    )

                elif op == '&':

                    stack.append(
                        'f' if 'f' in vals else 't'
                    )

                else:  # '|'

                    stack.append(
                        't' if 't' in vals else 'f'
                    )

        return stack[-1] == 't'