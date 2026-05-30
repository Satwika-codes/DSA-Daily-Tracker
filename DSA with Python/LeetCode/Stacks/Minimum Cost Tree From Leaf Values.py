# PROBLEM NUMBER: 1130
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# 1130. Minimum Cost Tree From Leaf Values
# DIFFICULTY: MEDIUM

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # Approach:
        # We use a Monotonic Decreasing Stack
        # to build the minimum-cost tree greedily.
        #
        # Key Insight:
        # Every leaf value will eventually be
        # multiplied exactly once with a larger
        # neighboring value.
        #
        # To minimize total cost, we should pair
        # smaller values with the smallest possible
        # larger value available.
        #
        # Step 1:
        # Initialize a decreasing stack with
        # a sentinel value (infinity).
        #
        # Step 2:
        # Traverse each number in the array.
        #
        # Step 3:
        # While current number is greater than
        # or equal to the stack top:
        #
        # • Pop the middle value.
        #
        # • This value must be combined with
        #   the smaller of its two larger neighbors:
        #
        #   min(left_greater, right_greater)
        #
        # • Add contribution:
        #
        #   mid * min(left_greater, right_greater)
        #
        # Step 4:
        # Push current number into stack.
        #
        # Step 5:
        # After traversal, some elements remain.
        #
        # • Pop remaining values one by one.
        #
        # • Multiply each with its nearest
        #   larger neighbor.
        #
        # Step 6:
        # Return the total minimum cost.

        # Sentinel value
        stack = [float('inf')]

        res = 0

        for num in arr:

            # Process smaller elements
            while stack[-1] <= num:

                mid = stack.pop()

                # Pair with smaller larger neighbor
                res += mid * min(stack[-1], num)

            stack.append(num)

        # Process remaining elements
        while len(stack) > 2:

            res += stack.pop() * stack[-1]

        return res