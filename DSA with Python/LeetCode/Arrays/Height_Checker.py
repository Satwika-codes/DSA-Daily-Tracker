# PROBLEM NUMBER: 1051
# https://leetcode.com/problems/height-checker/
# 1051. Height Checker
# DIFFICULTY: EASY
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        # Approach:
        # We need to count how many students are *not* standing in the correct
        # order if the line was sorted by height (non-decreasing order).
        #
        # Steps:
        # 1. Create a sorted copy of the heights array → `expected`.
        # 2. Compare each index in the original `heights` with `expected`.
        # 3. If they differ, this student is in the wrong position → increase count.
        #
        # Why it works:
        # - The sorted array represents the correct arrangement.
        # - Any mismatch indicates the student must be moved.
        #
        # Time Complexity:
        #   Sorting takes O(n log n), comparing takes O(n).
        # Space Complexity:
        #   O(n) for the sorted copy.

        expected = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count
