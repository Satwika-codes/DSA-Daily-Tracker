# PROBLEM NUMBER: 2972
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays/
# 2972.Count The No Of Incremovable Subarrays II
# DIFFICULTY: HARD
class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # - A subarray is incremovable if removing it makes the remaining array strictly increasing.
        # - First, find the longest strictly increasing prefix.
        # - If the entire array is already strictly increasing:
        #     → every subarray removal is valid
        #     → answer = n * (n + 1) // 2
        # - Otherwise:
        #     - Find the longest strictly increasing suffix.
        #     - Try removing subarrays between prefix and suffix.
        #     - Use two pointers to count valid removals efficiently.
        
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        
        n = len(nums)
        
        # Step 1: Find increasing prefix
        left = 0
        while left + 1 < n and nums[left] < nums[left + 1]:
            left += 1
        
        # If whole array is strictly increasing
        if left == n - 1:
            return n * (n + 1) // 2
        
        # Step 2: Find increasing suffix
        right = n - 1
        while right > 0 and nums[right - 1] < nums[right]:
            right -= 1
        
        ans = n - right + 1  # removing prefix entirely
        
        # Step 3: Two-pointer merge check
        i = 0
        j = right
        while i <= left:
            while j < n and nums[i] >= nums[j]:
                j += 1
            ans += n - j + 1
            i += 1
        
        return ans
