# PROBLEM NUMBER: 26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 26. Remove Duplicates from Sorted Array
# DIFFICULTY: Easy
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # - Problem: Remove duplicates from a sorted array **in-place** and return the count of unique elements.
        # - Use **two pointers**:
        #   • `i` scans through the array.  
        #   • `k` marks the position of the next unique element.
        # - Start with `k = 1` since the first element is always unique.
        # - For each `i` from 1 to end:
        #     - If `nums[i]` differs from the previous element, place it at `nums[k]` and increment `k`.
        # - After traversal, `k` represents the count of unique elements.
        # - The first `k` elements of `nums` will be the unique ones.
        # Time: O(n)  |  Space: O(1)
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k