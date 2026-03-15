# PROBLEMNUMBER: 2540
# https://leetcode.com/problems/minimum-common-value/
# 2540. Minimum Common Value
# DIFFICULTY: EASY
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Approach:
        # The arrays nums1 and nums2 are already sorted.
        # We use the two-pointer technique to find the smallest common element.
        
        # Step 1: Initialize two pointers:
        #         i → start of nums1
        #         j → start of nums2
        # Step 2: Compare nums1[i] and nums2[j].
        # Step 3: If they are equal → this is the smallest common element → return it.
        # Step 4: If nums1[i] < nums2[j], move pointer i forward.
        #         (because nums1[i] cannot match any smaller value in nums2)
        # Step 5: Otherwise move pointer j forward.
        # Step 6: Continue until one array finishes.
        # Step 7: If no common element is found → return -1.
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1