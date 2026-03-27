# PROBLEM NUMBER: 689
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# Maximum Sum of 3 Non-Overlapping Subarrays
# DIFFICULTY: HARD
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Approach:
        # We need to find 3 non-overlapping subarrays of size k
        # such that their total sum is maximized.
        #
        # Step 1: Compute sum of all subarrays of size k
        #         using sliding window → store in windowSum[]
        #
        # Step 2: Build 'left' array:
        #         • left[i] = index of maximum window sum from 0 to i
        #
        # Step 3: Build 'right' array:
        #         • right[i] = index of maximum window sum from i to end
        #         • In case of tie, choose smaller index for lexicographically smallest result
        #
        # Step 4: Iterate middle subarray index j:
        #         • j ranges from k to len(windowSum) - k - 1
        #
        # Step 5: For each j:
        #         • i = best left subarray → left[j - k]
        #         • l = best right subarray → right[j + k]
        #
        # Step 6: Compute total:
        #         windowSum[i] + windowSum[j] + windowSum[l]
        #
        # Step 7: Track maximum total and store indices [i, j, l]
        #
        # Step 8: Return the result.

        n = len(nums)

        # Step 1: window sums
        windowSum = [0] * (n - k + 1)
        curr = sum(nums[:k])
        windowSum[0] = curr

        for i in range(1, n - k + 1):
            curr += nums[i + k - 1] - nums[i - 1]
            windowSum[i] = curr

        # Step 2: best from left
        left = [0] * len(windowSum)
        best = 0
        for i in range(len(windowSum)):
            if windowSum[i] > windowSum[best]:
                best = i
            left[i] = best

        # Step 3: best from right
        right = [0] * len(windowSum)
        best = len(windowSum) - 1
        for i in range(len(windowSum) - 1, -1, -1):
            if windowSum[i] >= windowSum[best]:
                best = i
            right[i] = best

        # Step 4: try middle
        max_total = 0
        ans = [-1, -1, -1]

        for j in range(k, len(windowSum) - k):
            i = left[j - k]
            l = right[j + k]

            total = windowSum[i] + windowSum[j] + windowSum[l]

            if total > max_total:
                max_total = total
                ans = [i, j, l]

        return ans