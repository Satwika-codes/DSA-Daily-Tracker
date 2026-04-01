# PROBLEM NUMBER: 1425
# https://leetcode.com/problems/constrained-subsequence-sum/
# Constrained Subsequence Sum
# DIFFICULTY: HARD
class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Approach:
        # We need to find the maximum sum of a subsequence such that:
        # • For every chosen element nums[i], the previous chosen element
        #   must be within k distance (i.e., j where i - j <= k)
        #
        # Step 1: Use DP where:
        #         • dp[i] represents the maximum sum of a valid subsequence ending at index i
        #
        # Step 2: For each index i:
        #         • We can either take nums[i] alone
        #         • Or extend the best subsequence within last k indices
        #           → dp[i] = nums[i] + max(dp[j]) where j ∈ [i-k, i-1]
        #
        # Step 3: To efficiently get max(dp[j]) in window of size k:
        #         • Use a deque (monotonic decreasing) storing indices of dp
        #         • Front of deque always gives index of maximum dp value
        #
        # Step 4: Before processing index i:
        #         • Remove indices from deque that are out of window (i - k)
        #
        # Step 5: Compute dp[i]:
        #         • Start with nums[i]
        #         • If deque is not empty, add dp[dq[0]] (maximum in window)
        #
        # Step 6: Maintain deque in decreasing order of dp values:
        #         • Remove indices from back while dp[last] <= dp[i]
        #
        # Step 7: Only push index i into deque if dp[i] > 0
        #         • Because negative values won't help future sums
        #
        # Step 8: Keep track of overall maximum result
        #
        # Step 9: Return the result

        n = len(nums)
        dp = [0] * n
        dq = deque()  # stores indices, decreasing dp values

        res = nums[0]

        for i in range(n):
            # remove out-of-window indices
            while dq and dq[0] < i - k:
                dq.popleft()

            # compute dp[i]
            dp[i] = nums[i]
            if dq:
                dp[i] = max(dp[i], nums[i] + dp[dq[0]])

            # maintain decreasing deque
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            # only add if dp[i] > 0
            if dp[i] > 0:
                dq.append(i)

            res = max(res, dp[i])

        return res