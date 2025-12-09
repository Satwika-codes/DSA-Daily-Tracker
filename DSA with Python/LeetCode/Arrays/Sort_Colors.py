# PROBLEM NUMBER: 75
# https://leetcode.com/problems/sort-colors/
# 75.Sort Colors
# DIFFICULTY: MEDIUM
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Approach (Dutch National Flag Algorithm):
        # We maintain three pointers:
        # low  → boundary for placing 0s
        # mid  → current index being processed
        # high → boundary for placing 2s
        #
        # Rules:
        # 1. If nums[mid] == 0 → swap with low, move both low and mid forward.
        # 2. If nums[mid] == 1 → correct position, just move mid forward.
        # 3. If nums[mid] == 2 → swap with high, move high backward (mid stays).
        #
        # This ensures a single-pass O(n) sort without extra memory.

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Place 0 at the low position and expand the low region
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # 1 is already in the correct middle zone
                mid += 1

            else:  # nums[mid] == 2
                # Place 2 at the high position and shrink the high region
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
