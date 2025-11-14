# PROBLEM NUMBER: 414
# https://leetcode.com/problems/third-maximum-number/
# 414. Third Maximum Number
# DIFFICULTY: EASY
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # APPROACH (Track Top 3 Distinct Maximum Numbers):
        # Goal: Return the *third distinct* maximum number.
        #       If it does not exist, return the maximum.
        # Strategy:
        #  Maintain three variables: first, second, third (all start as None)
        #  Loop through each number:
        #       - Skip if number is already equal to any of first/second/third (to ensure distinctness)
        #       - Update first, second, third in the correct order whenever a new larger number appears.
        # Example:
        # nums = [3, 2, 1]
        # first = 3, second = 2, third = 1 → return 1
        # nums = [1, 2]
        # Only two distinct → return max = 2
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        first = second = third = None
        for x in nums:
            if x == first or x == second or x == third:
                continue
            if first is None or x > first:
                first, second, third = x, first, second
            elif second is None or x > second:
                second, third = x, second
            elif third is None or x > third:
                third = x
        return third if third is not None else first