# PROBLEM NUMBER: 241
# https://leetcode.com/problems/different-ways-to-add-parentheses/
# 241. Different Ways to Add Parentheses
# DIFFICULTY: MEDIUM
class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # Approach:
        # - Use Divide & Conquer with memoization.
        # - For every operator, split expression into left and right parts.
        # - Recursively compute all results from left and right, then combine using the operator.
        # - Memoize results for subexpressions to avoid recomputation.
        # Time: O(n * 2^n), Space: O(2^n)
        memo = {}

        def ways(expr):
            if expr.isdigit():
                return [int(expr)]
            if expr in memo:
                return memo[expr]

            res = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    left = ways(expr[:i])
                    right = ways(expr[i+1:])
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            else:
                                res.append(l * r)
            memo[expr] = res
            return res

        return ways(expression)
        