# PROBLEM NUMBER: 747
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# 747. Largest Number At Least Twice of Others
# DIFFICULTY: EASY
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # -------------------------
        # APPROACH
        # -------------------------
        # 1. Find the maximum element and its index.
        # 2. Check if this maximum element is at least twice every other element.
        # 3. If any element violates the condition (max < 2 * num), return -1.
        # 4. Otherwise, return the index of the maximum element.
        #
        # Why this works:
        # - The dominant element must be ≥ 2 * every other number.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        if not nums:
            return -1

        max_val = max(nums)
        max_idx = nums.index(max_val)

        # Check dominance condition
        for i, num in enumerate(nums):
            if i != max_idx and max_val < 2 * num:
                return -1

        return max_idx
