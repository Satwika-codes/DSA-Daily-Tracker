# PROBLEM NUMBER: 162
# https://leetcode.com/problems/find-peak-element/
# 162. Find Peak Element
# DIFFICULTY: MEDIUM
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # Use Binary Search to find a "peak" element.
        #
        # Key Idea:
        # - If nums[mid] > nums[mid + 1], the peak lies in the left half
        #   (including mid). So move r = mid.
        # - Else the peak lies in the right half, so move l = mid + 1.
        #
        # This works because:
        # - Whenever nums[mid] < nums[mid + 1], the slope is rising -> a peak exists right side.
        # - Whenever nums[mid] > nums[mid + 1], the slope is falling -> a peak exists left side.
        #
        # Time Complexity: O(log n)
        # Space Complexity: O(1)

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # If mid is greater than its right neighbor,
            # the peak must be on the left side.
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l   # l (or r) will be at the peak index
