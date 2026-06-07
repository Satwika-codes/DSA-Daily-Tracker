# PROBLEM NUMBER: 918
# https://leetcode.com/problems/maximum-sum-circular-subarray/
# 918. Maximum Sum Circular Subarray
# DIFFICULTY: MEDIUM

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # The maximum subarray in a circular
        # array can either be a normal subarray
        # or a wrap-around subarray.
        #
        # First, use Kadane's Algorithm to find
        # the maximum subarray sum normally.
        #
        # Then find the minimum subarray sum
        # using a modified Kadane's Algorithm.
        #
        # If we remove the minimum subarray
        # from the total array sum, the remaining
        # elements form the best circular
        # subarray sum.
        #
        # Therefore:
        # Circular Sum = Total Sum - Min Subarray Sum
        #
        # The answer is the maximum of the
        # normal subarray sum and the circular
        # subarray sum.
        #
        # If all elements are negative, return
        # the normal maximum subarray sum.

        total = sum(nums)

        # Maximum subarray (Kadane)
        cur_max = max_sum = nums[0]

        for x in nums[1:]:

            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)

        # Minimum subarray (Kadane variant)
        cur_min = min_sum = nums[0]

        for x in nums[1:]:

            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)

        # All elements negative
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)