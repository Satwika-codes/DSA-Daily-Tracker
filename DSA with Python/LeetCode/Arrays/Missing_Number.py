# PROBLEM NUMBER: 268
# https://leetcode.com/problems/missing-number/
# 268. Missing Number
# DIFFICULTY: EASY
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # APPROACH:
        # 1. Calculate the expected sum of numbers from 0 to n using formula: n*(n+1)//2
        # 2. Calculate the actual sum of numbers present in the array.
        # 3. The missing number is the difference: expected_sum - actual_sum.
        # Time Complexity: O(n) — sum(nums) iterates through all elements once.
        # Space Complexity: O(1) — no extra space is used besides variables.
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)