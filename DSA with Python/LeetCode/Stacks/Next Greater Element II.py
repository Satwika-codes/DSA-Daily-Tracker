# PROBLEM NUMBER: 503
# https://leetcode.com/problems/next-greater-element-ii/
# 503. Next Greater Element II
# DIFFICULTY: MEDIUM

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Approach:
        # We use a Monotonic Decreasing Stack
        # to find the next greater element for
        # each index in a circular array.
        #
        # Key Insight:
        # Since the array is circular,
        # after reaching the last element,
        # we continue searching from the beginning.
        #
        # To simulate this behavior,
        # we iterate through the array twice.
        #
        # Step 1:
        # Initialize:
        #
        # • res = [-1] * n
        #   Stores answers.
        #
        # • stack
        #   Stores indices whose next greater
        #   element has not been found yet.
        #
        # Step 2:
        # Traverse from 0 to (2*n - 1).
        #
        # Current element:
        # nums[i % n]
        #
        # This wraps around the array.
        #
        # Step 3:
        # While current element is greater than
        # the element at the index on stack top:
        #
        # • Pop index
        # • Current element becomes its answer
        #
        # Step 4:
        # During the first pass only:
        #
        # • Push indices into stack
        #
        # We do not push during the second pass
        # because all indices are already stored.
        #
        # Step 5:
        # Any remaining indices in stack
        # have no greater element,
        # so their answer remains -1.
        #
        # Step 6:
        # Return result array.

        n = len(nums)

        res = [-1] * n

        # Stores indices
        stack = []

        # Traverse twice for circular behavior
        for i in range(2 * n):

            # Resolve next greater elements
            while stack and nums[stack[-1]] < nums[i % n]:

                idx = stack.pop()

                res[idx] = nums[i % n]

            # Push only during first pass
            if i < n:
                stack.append(i)

        return res