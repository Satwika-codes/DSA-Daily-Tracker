# PROBLEM NUMBER: 283
# https://leetcode.com/problems/move-zeroes/
# 283. Move Zeroes
# DIFFICULTY: EASY
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # APPROACH (Two-pointer technique):
        # 1. Use two pointers — i for scanning elements and j for tracking the next non-zero position.
        # 2. Traverse through nums:
        #       - When a non-zero element is found at i, swap it with nums[j].
        #       - Increment j to move the boundary of non-zero elements forward.
        # 3. This pushes all zeros to the end while maintaining the order of non-zero elements.
        # Example:
        # nums = [0,1,0,3,12]
        # After moving zeros → [1,3,12,0,0]
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1