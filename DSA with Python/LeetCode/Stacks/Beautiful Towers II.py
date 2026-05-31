# PROBLEM NUMBER: 2865
# https://leetcode.com/problems/beautiful-towers-i/
# 2865. Beautiful Towers I
# DIFFICULTY: MEDIUM

class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        """
        :type maxHeights: List[int]
        :rtype: int
        """

        # Approach:
        # We treat every index as the peak
        # of a beautiful tower arrangement.
        #
        # Rules:
        #
        # • Heights must not exceed maxHeights[i]
        #
        # • Moving away from the peak,
        #   heights must be non-increasing
        #   on both sides.
        #
        # Goal:
        # Find the maximum possible sum
        # of tower heights.
        #
        # Key Insight:
        # For every index i, compute:
        #
        # • left[i]
        #   Contribution from the left side
        #   when i acts as a peak.
        #
        # • right[i]
        #   Contribution from the right side
        #   when i acts as a peak.
        #
        # We use Monotonic Increasing Stacks
        # to efficiently find the nearest
        # smaller-or-equal height.
        #
        # Step 1:
        # Compute left contributions.
        #
        # If a previous smaller-or-equal
        # element exists:
        #
        # • Reuse its contribution.
        #
        # • Extend using current height.
        #
        # Otherwise:
        #
        # • Current height controls
        #   the entire prefix.
        #
        # Step 2:
        # Compute right contributions
        # similarly by traversing from
        # right to left.
        #
        # Step 3:
        # Consider each index as the peak.
        #
        # Total height sum:
        #
        # left[i] + right[i] - maxHeights[i]
        #
        # Peak is subtracted once because
        # it is counted in both arrays.
        #
        # Step 4:
        # Return the maximum value.

        n = len(maxHeights)

        left = [0] * n
        stack = []

        # Left contribution
        for i in range(n):

            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()

            if stack:

                prev = stack[-1]

                left[i] = (
                    left[prev]
                    + (i - prev) * maxHeights[i]
                )

            else:

                left[i] = (i + 1) * maxHeights[i]

            stack.append(i)

        right = [0] * n
        stack = []

        # Right contribution
        for i in range(n - 1, -1, -1):

            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()

            if stack:

                nxt = stack[-1]

                right[i] = (
                    right[nxt]
                    + (nxt - i) * maxHeights[i]
                )

            else:

                right[i] = (n - i) * maxHeights[i]

            stack.append(i)

        ans = 0

        # Try every index as peak
        for i in range(n):

            ans = max(
                ans,
                left[i] + right[i] - maxHeights[i]
            )

        return ans