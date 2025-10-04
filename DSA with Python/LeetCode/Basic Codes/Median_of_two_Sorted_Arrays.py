# PROBLEM NUMBER: 4
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# DIFFICULTY: HARD
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        Approach:
        - Combine both arrays into a single list `total_arr`.
        - Sort the combined list.
        - If the length of `total_arr` is 0, return None (edge case).
        - Find the middle index.
        - If the total length is odd → return the middle element.
        - If the total length is even → return the average of the two middle elements.

        Time Complexity: O((m+n) log(m+n)) due to sorting.
        Space Complexity: O(m+n) since we build a combined array.
        (This works correctly but is not optimal. The optimal solution uses binary search in O(log(min(m,n))).)
        """
        total_arr=nums1+nums2
        total_arr.sort()
        if(len(total_arr))==0:
            return None
        mid=len(total_arr)//2
        if len(total_arr)% 2 != 0:
            return total_arr[mid]
        else:
            return (total_arr[mid-1]+total_arr[mid])/2.0



