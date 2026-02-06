# PROBLEM NUMBER: 581
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# 581.Shortest Unsorted Continuous Subarray
# DIFFICULTY: HARD
class Solution(object):
    def findUnsortedSubarray(self, nums):
        
        # Approach:
        # - Traverse from left to right to find the last index where the array
        #   is not increasing → this gives the right boundary.
        # - Traverse from right to left to find the first index where the array
        #   is not decreasing → this gives the left boundary.
        # - If the array is already sorted, return 0.

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        n = len(nums)
        left, right = -1, -2
        max_seen = nums[0]
        min_seen = nums[-1]

        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i

        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                left = i

        return right - left + 1
