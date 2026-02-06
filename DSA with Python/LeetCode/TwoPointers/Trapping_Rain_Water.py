# PROBLEM NUMBER: 42
# https://leetcode.com/problems/trapping-rain-water/
# 42. Trapping Rain Water
# DIFFICULTY: HARD
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Approach:
        # ---------
        # This problem is solved using the Two Pointers technique.

        # 1. Use two pointers:
        #    - left starting from the beginning of the array
        #    - right starting from the end of the array
        # 2. Maintain two variables:
        #    - left_max: maximum height encountered from the left
        #    - right_max: maximum height encountered from the right
        # 3. Water trapped at any position depends on the minimum of
        #    left_max and right_max minus the height at that position.
        # 4. Move the pointer with the smaller height:
        #    - If height[left] < height[right], process the left side
        #    - Otherwise, process the right side
        # 5. Update left_max or right_max accordingly and add trapped
        #    water when the current height is smaller than the max so far.
        # 6. Continue until the two pointers meet.

        # This approach works in O(n) time and O(1) extra space.
        

        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        
        return water
