# PROBLEM NUMBER: 2866
# https://leetcode.com/problems/beautiful-towers-ii/
# 2866. Beautiful Towers II
# DIFFICULTY: HARD

class Solution(object):
    def maximumSumOfHeights(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        # Approach:
        # We treat every index as the peak
        # of a beautiful tower arrangement.
        #
        # For a chosen peak:
        #
        # • Heights must be non-increasing
        #   when moving away from the peak
        #   towards the left.
        #
        # • Heights must be non-increasing
        #   when moving away from the peak
        #   towards the right.
        #
        # Goal:
        # Find the maximum possible total
        # sum of tower heights.
        #
        # Key Insight:
        # For each position, we need:
        #
        # • Sum contribution from left side
        # • Sum contribution from right side
        #
        # These can be computed efficiently
        # using Monotonic Increasing Stacks.
        #
        # Step 1:
        # Compute left[i]:
        #
        # left[i] = maximum valid sum
        # considering index i as the rightmost point.
        #
        # Maintain a monotonic stack.
        #
        # Find the previous smaller-or-equal height.
        #
        # If such index exists:
        #
        # Use its previously computed contribution
        # and extend using current height.
        #
        # Otherwise:
        #
        # Current height controls the entire prefix.
        #
        # Step 2:
        # Compute right[i]:
        #
        # Similar logic but process from
        # right to left.
        #
        # Find next smaller-or-equal height
        # using another monotonic stack.
        #
        # Step 3:
        # Treat each index as peak.
        #
        # Total contribution:
        #
        # left[i] + right[i] - heights[i]
        #
        # We subtract heights[i]
        # because peak is counted twice.
        #
        # Step 4:
        # Return the maximum value obtained.

        n = len(heights)

        left = [0] * n
        stack = []

        # Contribution from left side
        for i in range(n):

            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()

            if stack:

                prev = stack[-1]

                left[i] = (
                    left[prev]
                    + (i - prev) * heights[i]
                )

            else:

                left[i] = (i + 1) * heights[i]

            stack.append(i)

        right = [0] * n
        stack = []

        # Contribution from right side
        for i in range(n - 1, -1, -1):

            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()

            if stack:

                nxt = stack[-1]

                right[i] = (
                    right[nxt]
                    + (nxt - i) * heights[i]
                )

            else:

                right[i] = (n - i) * heights[i]

            stack.append(i)

        ans = 0

        # Consider each index as peak
        for i in range(n):

            ans = max(
                ans,
                left[i] + right[i] - heights[i]
            )

        return ans