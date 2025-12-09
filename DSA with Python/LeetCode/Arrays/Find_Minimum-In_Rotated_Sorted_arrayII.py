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
        # Step 1: Use binary search on the rotated sorted array (may contain duplicates).
        # Step 2: Compare nums[mid] with nums[right]:
        #         - If nums[mid] < nums[right], the minimum lies in the left half → move right = mid.
        #         - If nums[mid] > nums[right], the minimum lies in the right half → move left = mid + 1.
        #         - If nums[mid] == nums[right], duplicates make it unclear → safely shrink right -= 1.
        # Step 3: Continue until left == right.
        # Step 4: At the end, nums[left] is the minimum element.

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1

        return nums[left]
