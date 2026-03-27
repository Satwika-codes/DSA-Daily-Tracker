# PROBLEM NUMBER: 1499
# https://leetcode.com/problems/max-value-of-equation/
# 1499. Max Value of Equation
# DIFFICULTY: HARD
from collections import deque

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """

        # Approach:
        # We need to maximize:
        #     yi + yj + |xi - xj|
        #
        # Since points are sorted and xi < xj:
        #     |xi - xj| = xj - xi
        #
        # So equation becomes:
        #     (yi - xi) + (yj + xj)
        #
        # Step 1: Traverse all points (x, y).
        #
        # Step 2: Maintain a deque storing pairs:
        #         (yi - xi, xi), in decreasing order of (yi - xi).
        #
        # Step 3: Remove points from front if they are out of valid range:
        #         • Condition: current x - xi > k
        #
        # Step 4: If deque is not empty:
        #         • The front gives maximum (yi - xi)
        #         • Compute candidate:
        #           dq[0][0] + x + y
        #         • Update result
        #
        # Step 5: Maintain monotonic decreasing order in deque:
        #         • Remove elements from back if their (y - x)
        #           is <= current (y - x)
        #
        # Step 6: Add current point (y - x, x) into deque.
        #
        # Step 7: Return the maximum value found.

        dq = deque()  # stores (yi - xi, xi)
        res = float('-inf')

        for x, y in points:

            # Remove points out of range
            while dq and x - dq[0][1] > k:
                dq.popleft()

            # Compute answer using best candidate
            if dq:
                res = max(res, dq[0][0] + x + y)

            # Maintain decreasing order of (y - x)
            while dq and dq[-1][0] <= y - x:
                dq.pop()

            dq.append((y - x, x))

        return res