# PROBLEM NUMBER:2334
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/v
# 2334. Subarray With Elements Greater Than Varying Threshold
# DIFFICULTY: HARD
class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        # Approach:
        # We need a subarray of size k such that:
        # minimum_element * k > threshold
        #
        # Key Idea:
        # Treat each element as possible minimum of a subarray
        # and find the largest window where it remains minimum.
        #
        # Step 1: Use monotonic stack to find:
        #         • previous smaller element index
        #         • next smaller element index
        #
        # Step 2: For each index i:
        #         • left[i] = previous smaller index
        #         • right[i] = next smaller index
        #
        # Step 3: Compute maximum window where nums[i]
        #         is the minimum:
        #         width = right[i] - left[i] - 1
        #
        # Step 4: Check condition:
        #         nums[i] * width > threshold
        #
        # Step 5: If condition holds:
        #         • width is valid subarray size
        #         • return width
        #
        # Step 6: If none works, return -1

        n = len(nums)

        left = [-1] * n
        right = [n] * n

        stack = []

        # previous smaller
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)

        stack = []

        # next smaller
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]

            stack.append(i)

        for i in range(n):
            width = right[i] - left[i] - 1

            if nums[i] * width > threshold:
                return width

        return -1