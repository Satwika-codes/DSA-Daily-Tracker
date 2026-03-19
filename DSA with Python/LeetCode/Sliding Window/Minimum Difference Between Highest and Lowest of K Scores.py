# PROBLEM NUMBER: 1984
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
# Minimum Difference Between Highest and Lowest of K Scores
# DIFFICULTY:EASY
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Approach:
        # We need to select any k elements such that the difference
        # between the maximum and minimum among them is minimized.
        #
        # Step 1: If k == 1, return 0 because a single element
        #         has no difference.
        #
        # Step 2: Sort the array so that elements are in increasing order.
        #
        # Step 3: Use a sliding window of size k:
        #         For each window, compute the difference between
        #         the last and first element (max - min).
        #
        # Step 4: Keep track of the minimum difference found.
        #
        # Step 5: Return the minimum difference.

        if k == 1:
            return 0

        nums.sort()
        min_diff = float('inf')

        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)

        return min_diff