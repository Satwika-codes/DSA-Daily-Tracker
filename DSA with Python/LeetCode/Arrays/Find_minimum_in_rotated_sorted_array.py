# PROBLEM NUMBER: 153
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 153. Find Minimum in Rotated Sorted Array
# DIFFICULTY: MEDIUM
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # We use binary search because the array is a rotated sorted array.
        #
        # Key observations:
        # 1. If nums[mid] > nums[right], it means the minimum lies in the right half.
        #    → So move left = mid + 1
        #
        # 2. Otherwise, the minimum is in the left half (including mid).
        #    → So move right = mid
        #
        # The loop continues until left == right,
        # and that position will be the index of the minimum element.
        #
        # Time Complexity: O(log n)

        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
