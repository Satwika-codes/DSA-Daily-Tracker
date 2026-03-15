# PROBLEM NUMBER: 2441
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
# 2441. Largest Positive Integer That Exists With Its Negative
# DIFFICULTY: EASY
class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # Step 1: We need to find the largest positive integer k such that both k and -k exist in the array.
        # Step 2: Convert the list into a set so we can check existence in O(1) time.
        # Step 3: Initialize max_k = -1 (because if no such pair exists, we must return -1).
        # Step 4: Iterate through each number in nums.
        # Step 5: Only consider positive numbers (since we want the largest positive k).
        # Step 6: For each positive number num, check if its negative (-num) exists in the set.
        # Step 7: If it exists, update max_k = max(max_k, num).
        # Step 8: After checking all numbers, return max_k.
        seen = set(nums)
        max_k = -1

        for num in nums:
            if num > 0 and -num in seen:
                max_k = max(max_k, num)

        return max_k