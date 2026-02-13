# PROBLEM NUMBER: 3194
# https://leetcode.com/problems/minimum-average-of-smallest-largest-elements/
# 3194. Minimum Average of Smallest and Largest Elements
# DIFFICULTY: EASY
class Solution(object):
    def minimumAverage(self, nums):
        
        # Approach:
        # 1. Sort the array.
        # 2. Use two pointers:
        #    - One at the smallest element (left).
        #    - One at the largest element (right).
        # 3. Compute the average of nums[left] and nums[right].
        # 4. Move inward (left++, right--) and keep calculating averages.
        # 5. Return the minimum average found.

        # Time Complexity: O(n log n)  (due to sorting)
        # Space Complexity: O(1)
        
        
        nums.sort()
        left, right = 0, len(nums) - 1
        min_avg = float('inf')
        
        while left < right:
            avg = (nums[left] + nums[right]) / 2.0
            min_avg = min(min_avg, avg)
            left += 1
            right -= 1
        
        return min_avg
