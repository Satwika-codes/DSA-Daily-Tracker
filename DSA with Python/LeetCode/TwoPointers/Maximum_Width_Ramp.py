# PROBLEM NUMBER: 1352
# https://leetcode.com/problems/maximum-width-ramp/
# 1352. Maximum Width Ramp
# DIFFICULTY: HARD
class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # Step 1: The goal is to find the maximum width ramp, which is defined as a pair of indices (i, j) such that i < j and nums[i] <= nums[j], and we want to maximize the width j - i.
        # Step 2: First create a monotonic decreasing stack that stores indices of elements. This stack keeps track of potential starting positions `i` for ramps where each stored index corresponds to a value smaller than all previous ones.
        # Step 3: Traverse the array from left to right and push an index `i` into the stack only if the stack is empty or the current value is smaller than the value at the index on top of the stack. This ensures the stack stores indices of strictly decreasing values.
        # Step 4: After building the stack, traverse the array from right to left using index `j`. This allows us to try forming ramps with the farthest possible right endpoint first, maximizing the width.
        # Step 5: While the stack is not empty and the value at `nums[j]` is greater than or equal to the value at the index on top of the stack, we have found a valid ramp.
        # Step 6: Pop the index `i` from the stack and calculate the width `j - i`, then update `max_width` if this width is larger than the current maximum.
        # Step 7: Continue popping while the condition holds because the current `j` may form valid ramps with multiple indices stored in the stack.
        # Step 8: Continue scanning the array from right to left until all indices are processed.
        # Step 9: Finally return `max_width`, which represents the largest width ramp found in the array.

        n = len(nums)
        stack = []

        # Step 1: Build decreasing stack
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        max_width = 0

        # Step 2: Traverse from right
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)

        return max_width