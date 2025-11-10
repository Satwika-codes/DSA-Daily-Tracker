# PROBLEM NUMBER: 53
# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray
# DIFFICULTY: MEDIUM
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Approach:
        # We use Kadane’s Algorithm to find the maximum sum subarray in O(n) time.
        # Initialize two variables:
        #     - curr_sum → stores current subarray sum.
        #     - max_sum  → stores the maximum subarray sum so far.
        #    Both start as the first element.
        # For each element, decide:
        #     - Start a new subarray from nums[i], OR
        #     - Extend the previous subarray by adding nums[i].
        #    (curr_sum = max(nums[i], curr_sum + nums[i]))
        # Update the global maximum each time:
        #    (max_sum = max(max_sum, curr_sum))
        #Finally, return max_sum as the result.
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum