# PROBLEM NUMBER: 3523
# https://leetcode.com/problems/make-array-non-decreasing/
# 2523.Make Array Non-decreasing
# DIFFICULTY: MEDIUM

class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # We use a stack to maintain valid segments.
        #
        # Key Idea:
        # The final array must satisfy the required
        # ordering condition after performing merges.
        #
        # Whenever the order is violated,
        # we merge segments until the condition
        # becomes valid again.
        #
        # Step 1:
        # Traverse each element in nums.
        #
        # Step 2:
        # Treat the current element as the
        # value of a new segment.
        #
        # Step 3:
        # If the top segment in the stack is
        # greater than the current segment:
        #
        # • The order breaks.
        #
        # • Merge the two segments.
        #
        # • The merged segment value becomes
        #   the maximum of both segments.
        #
        # • Continue merging while the order
        #   remains invalid.
        #
        # Step 4:
        # Push the final merged segment
        # back into the stack.
        #
        # Step 5:
        # After processing all elements,
        # each stack entry represents one
        # segment in the final array.
        #
        # Step 6:
        # Return the number of segments.

        stack = []

        for x in nums:

            # Current segment value
            cur = x

            # Merge while ordering breaks
            while stack and stack[-1] > cur:

                cur = max(
                    cur,
                    stack.pop()
                )

            stack.append(cur)

        return len(stack)