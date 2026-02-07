# PROBLEM NUMBER:658
# https://leetcode.com/problems/find-k-closest-elements/
# 658.Find K closest elements
# DIFFICULTY:MEDIUM
class Solution(object):
    def findClosestElements(self, arr, k, x):
        
        # Approach:
        # ---------
        # Since the array is already sorted, we can use Binary Search.

        # Idea:
        # - We want to find a window of size `k`
        # - This window should contain the `k` elements closest to `x`
        # - We binary search on the starting index of the window

        # Logic:
        # - Search space for left boundary is from 0 to len(arr) - k
        # - For a mid index, compare:
        #       x - arr[mid]  and  arr[mid + k] - x
        # - If left side is farther, move right
        # - Else, move left

        # Time Complexity:
        # - O(log(n - k)) for binary search
        # - O(k) for returning result

        # Space Complexity:
        # - O(1) extra space
        """

        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
