# PROBLEM NUMBER: 349
# https://leetcode.com/problems/intersection-of-two-arrays/
# 349.Intersection of Two Arrays
# DIFFICULTY: EASY
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # -------------------------
        # APPROACH
        # -------------------------
        # 1. Loop through each element in nums1.
        # 2. If the element exists in nums2 AND is not already in result list,
        #    add it to the result.
        #
        # Key Idea:
        # - We are manually ensuring uniqueness (x not in res).
        # - Uses direct list lookup, so it's simpler but less efficient.
        #
        # Time Complexity: O(n * m)   (because "x in nums2" is O(m))
        # Space Complexity: O(k)      (k = size of intersection)
        #
        # Note: A more efficient approach uses sets, but here we keep your logic.
        # -------------------------

        res = []
        for x in nums1:
            if x in nums2 and x not in res:
                res.append(x)
        return res
