# PROBLEM NUMBER: 736
# https://leetcode.com/problems/parse-lisp-expression/
# 736. Parse Lisp Expression
# DIFFICULTY: HARD

class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """

        # Approach:
        # We recursively evaluate the Lisp expression
        # while maintaining variable scopes.
        #
        # Supported Operations:
        #
        # • add
        #   (add x y)
        #   → x + y
        #
        # • mult
        #   (mult x y)
        #   → x * y
        #
        # • let
        #   (let v1 e1 v2 e2 ... expr)
        #   → Assign variables and evaluate final expression
        #
        # Key Idea:
        # Variables have local scope.
        # Whenever we enter a new expression,
        # we create a copy of the current scope.
        #
        # Step 1:
        # If expression is not enclosed in parentheses:
        #
        # • If it is a number → return integer value
        #
        # • Otherwise it is a variable
        #   → return value from current scope
        #
        # Step 2:
        # Remove outer parentheses.
        #
        # Step 3:
        # Split expression into top-level parts.
        #
        # Example:
        # (add 1 (mult 2 3))
        #
        # becomes:
        # ["add", "1", "(mult 2 3)"]
        #
        # We track bracket balance to avoid
        # splitting inside nested expressions.
        #
        # Step 4:
        # Process operation:
        #
        # • add:
        #   Evaluate both operands and add.
        #
        # • mult:
        #   Evaluate both operands and multiply.
        #
        # • let:
        #   Create new scope.
        #   Assign variables one by one.
        #   Evaluate final expression using
        #   updated scope.
        #
        # Step 5:
        # Recursively evaluate nested expressions.
        #
        # Step 6:
        # Return final evaluated result.

        def eval_expr(expr, scope):

            # Number or variable
            if expr[0] != '(':

                # Numeric value
                if expr[0].isdigit() or expr[0] == '-':
                    return int(expr)

                # Variable lookup
                return scope[expr]

            # Remove outer parentheses
            expr = expr[1:-1]

            # Split expression into top-level tokens
            def split(expr):

                res = []
                bal = 0
                start = 0

                for i, ch in enumerate(expr):

                    if ch == '(':
                        bal += 1

                    elif ch == ')':
                        bal -= 1

                    elif ch == ' ' and bal == 0:
                        res.append(expr[start:i])
                        start = i + 1

                res.append(expr[start:])

                return res

            parts = split(expr)

            # add operation
            if parts[0] == 'add':
                return (
                    eval_expr(parts[1], dict(scope))
                    + eval_expr(parts[2], dict(scope))
                )

            # mult operation
            if parts[0] == 'mult':
                return (
                    eval_expr(parts[1], dict(scope))
                    * eval_expr(parts[2], dict(scope))
                )

            # let operation
            new_scope = dict(scope)

            i = 1

            while i < len(parts) - 1:

                var = parts[i]

                val = eval_expr(parts[i + 1], new_scope)

                new_scope[var] = val

                i += 2

            # Evaluate final expression
            return eval_expr(parts[-1], new_scope)

        return eval_expr(expression, {})