# PROBLEM NUMBER: 31
# https://leetcode.com/problems/next-permutation/
# 31. Next Permutation
# DIFFICULTY: MEDIUM
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Approach:
        # Traverse from the end to find the first index `i` where nums[i] < nums[i + 1].
        #     → This identifies the "pivot" where the next greater permutation can be formed.
        # If such `i` exists:
        #     - Find index `j` (from the end) where nums[j] > nums[i].
        #     - Swap nums[i] and nums[j].
        # Reverse the subarray after index `i` (i.e., nums[i+1:]) to get the smallest
        #     increasing order for the next permutation.
        # If no such `i` is found, the array is in descending order.
        #     → Reverse the entire array to get the smallest permutation.
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])


