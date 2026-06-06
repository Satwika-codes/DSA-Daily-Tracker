# PROBLEM NUMBER: 769
# https://leetcode.com/problems/max-chunks-to-make-sorted/
# 769. Max Chunks To Make Sorted
# DIFFICULTY: MEDIUM

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # Approach:
        # Traverse the array while tracking
        # the maximum value seen so far.
        #
        # A chunk can end at index i if all
        # elements that belong before or at
        # index i are already contained within
        # the current segment.
        #
        # This happens when the maximum value
        # seen so far equals the current index.
        #
        # At that point, sorting the current
        # chunk independently will place all
        # its elements in their correct positions.
        #
        # Count every such valid chunk boundary.

        max_so_far = 0
        chunks = 0

        for i in range(len(arr)):

            max_so_far = max(max_so_far, arr[i])

            if max_so_far == i:
                chunks += 1

        return chunks