# PROBLEM NUMBER: 2762
# https://leetcode.com/problems/continuous-subarrays/
# 2762. Continuous Subarrays
# DIFFICULTY: MEDIUM

from collections import deque

class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # We use a sliding window and maintain
        # the maximum and minimum elements in
        # the current window using two monotonic
        # deques.
        #
        # • maxdq stores indices in decreasing
        #   order, so its front always gives
        #   the maximum element.
        #
        # • mindq stores indices in increasing
        #   order, so its front always gives
        #   the minimum element.
        #
        # If the difference between the maximum
        # and minimum exceeds 2, shrink the
        # window from the left until it becomes
        # valid again.
        #
        # For every valid window ending at
        # index 'right', all subarrays starting
        # from left to right are valid.
        #
        # Add their count to the answer.

        maxdq = deque()  # decreasing
        mindq = deque()  # increasing

        left = 0
        ans = 0

        for right in range(len(nums)):

            while maxdq and nums[maxdq[-1]] < nums[right]:
                maxdq.pop()

            maxdq.append(right)

            while mindq and nums[mindq[-1]] > nums[right]:
                mindq.pop()

            mindq.append(right)

            while nums[maxdq[0]] - nums[mindq[0]] > 2:

                if maxdq[0] == left:
                    maxdq.popleft()

                if mindq[0] == left:
                    mindq.popleft()

                left += 1

            ans += right - left + 1

        return ans