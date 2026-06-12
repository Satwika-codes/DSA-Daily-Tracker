# PROBLEM NUMBER: 1696
# https://leetcode.com/problems/jump-game-vi/
# 1696. Jump Game VI
# DIFFICULTY: MEDIUM

from collections import deque

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Approach:
        # We use dynamic programming
        # where dp[i] represents the
        # maximum score that can be
        # obtained upon reaching index i.
        #
        # To reach index i, we can jump
        # from any index in the range
        # [i - k, i - 1].
        #
        # Therefore:
        # dp[i] = nums[i] +
        #         max(dp[j])
        # for all valid previous indices.
        #
        # To efficiently obtain the
        # maximum dp value in the last
        # k positions, we maintain a
        # monotonic deque.
        #
        # The deque stores indices in
        # decreasing order of their
        # dp values.
        #
        # For each index:
        # • Remove indices that are
        #   outside the current window.
        # • Use the front of the deque
        #   as the maximum dp value.
        # • Remove smaller dp values
        #   from the back since they
        #   can never be optimal later.
        #
        # The answer is dp[n - 1].
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        dq = deque([0])

        for i in range(1, n):

            while dq and dq[0] < i - k:
                dq.popleft()

            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

        return dp[-1]