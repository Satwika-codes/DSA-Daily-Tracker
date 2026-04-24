# PROBLEM NUMBER: 673
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# 673. Find Maximum Non-decreasing Subarray
# DIFFICULTY: HARD

class Solution(object):
    def findMaximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # We need maximum number of valid partitions such that
        # each next subarray sum is at least previous subarray sum.
        #
        # Step 1: Build prefix sum array:
        #         • Helps compute subarray sums quickly
        #
        # Step 2: Define:
        #         • dp[i] = maximum partitions using first i elements
        #
        # Step 3: Use pre[i]:
        #         • Stores best previous split point for index i
        #
        # Step 4: Traverse from 1 to n:
        #
        #         • Carry forward best split point
        #         • Compute:
        #             dp[i] = dp[pre[i]] + 1
        #
        # Step 5: Compute target prefix needed for next valid partition:
        #         target = 2 * prefix[i] - prefix[pre[i]]
        #
        # Step 6: Use binary search:
        #         • Find first index j where prefix[j] >= target
        #
        # Step 7: Update future transition:
        #         • pre[j] may use current i as a better split
        #
        # Step 8: Return dp[n]

        n = len(nums)

        # prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        # dp[i] = max length using first i elements
        dp = [0] * (n + 1)

        # pre[i] stores best split point
        pre = [0] * (n + 2)

        for i in range(1, n + 1):
            pre[i] = max(pre[i], pre[i-1])

            dp[i] = dp[pre[i]] + 1

            # push transition
            target = 2 * prefix[i] - prefix[pre[i]]
            j = bisect_left(prefix, target)

            if j <= n:
                pre[j] = max(pre[j], i)

        return dp[n]