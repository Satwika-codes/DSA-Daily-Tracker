# PROBLEM NUMBER: 561
# https://leetcode.com/problems/array-partition/
# 561.Array Partition
# DIFFICULTY: EASY
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # Problem wants us to form n pairs from 2n numbers such that
        # the sum of min(a, b) of all pairs is maximized.
        #
        # Key Insight:
        # - To maximize the sum of minimums, we sort the array.
        # - After sorting, pairing adjacent numbers gives the best result.
        # - The smaller number of each pair will always be the element at even indices.
        #
        # Steps:
        # 1. Sort the array.
        # 2. Add all elements at even indices (0, 2, 4, ...).
        #
        # Time Complexity: O(n log n) due to sorting.
        # Space Complexity: O(1) extra (ignoring sorting memory).

        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total
