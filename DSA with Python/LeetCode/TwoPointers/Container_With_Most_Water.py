# PROBLEM NUMBER: 11
# https://leetcode.com/problems/container-with-most-water/
# 11. Container With Most Water
# DIFFICULTY: MEDIUM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Approach:
        # Use two pointers starting from both ends.

        # - Calculate area using the shorter height.
        # - Move the pointer with the smaller height inward,
        #   because moving the taller one cannot increase area.
        # - Keep track of the maximum area found.

        # Time Complexity:
        # - O(n)

        # Space Complexity:
        # - O(1)

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            curr_area = min(height[left], height[right]) * width
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
