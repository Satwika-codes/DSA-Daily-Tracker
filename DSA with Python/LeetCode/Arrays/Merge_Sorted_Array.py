# PROBLEM NUMBER: 88
# https://leetcode.com/problems/merge-sorted-array/
# 88. Merge Sorted Array
# DIFFICULTY: EASY
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Approach:
        # Merge two sorted arrays (nums1 and nums2) into nums1 in non-decreasing order.
        # Start from the end of both arrays to avoid overwriting values in nums1.
        # Compare elements from the back and place the larger one at the end.
        # Continue until all elements from nums2 are placed in nums1.
        # Time Complexity: O(m + n)
        # Space Complexity: O(1)
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1