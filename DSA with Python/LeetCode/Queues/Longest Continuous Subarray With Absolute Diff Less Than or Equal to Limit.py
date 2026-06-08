# PROBLEM NUMBER: 1438
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# DIFFICULTY: MEDIUM

from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
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
        # and minimum exceeds the given limit,
        # shrink the window from the left until
        # it becomes valid again.
        #
        # For every valid window, update the
        # maximum length found so far.

        maxdq = deque()
        mindq = deque()

        left = 0
        ans = 0

        for right in range(len(nums)):

            while maxdq and nums[maxdq[-1]] < nums[right]:
                maxdq.pop()

            maxdq.append(right)

            while mindq and nums[mindq[-1]] > nums[right]:
                mindq.pop()

            mindq.append(right)

            while nums[maxdq[0]] - nums[mindq[0]] > limit:

                if maxdq[0] == left:
                    maxdq.popleft()

                if mindq[0] == left:
                    mindq.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans