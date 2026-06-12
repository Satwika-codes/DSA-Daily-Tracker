# PROBLEM NUMBER: 862
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# 862. Shortest Subarray with Sum at Least K
# DIFFICULTY: HARD

from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Approach:
        # We use prefix sums to quickly
        # calculate the sum of any
        # subarray.
        #
        # Let prefix[i] represent the
        # sum of the first i elements.
        #
        # For a subarray from j to i - 1:
        # sum = prefix[i] - prefix[j]
        #
        # We need the shortest subarray
        # whose sum is at least k.
        #
        # A monotonic deque is used to
        # store indices of prefix sums
        # in increasing order.
        #
        # For each prefix sum:
        # • While the current prefix sum
        #   forms a valid subarray with
        #   the front of the deque,
        #   update the answer and remove
        #   the front index.
        #
        # • Remove indices from the back
        #   whose prefix sums are greater
        #   than or equal to the current
        #   prefix sum, since they can
        #   never produce a shorter or
        #   better subarray in the future.
        #
        # This allows us to find the
        # shortest valid subarray in
        # linear time.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        ans = n + 1

        for i in range(n + 1):

            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())

            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return ans if ans <= n else -1