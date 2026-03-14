# PROBLEM NUMBER: 1574
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
# 1574.Shortest Subarray to be Removed to Make Array Sorted
# DIFFICULTY: MEDIUM
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # APPROACH:
        # Step 1: First determine the length of the array and try to identify the longest non-decreasing prefix from the start of the array. We move a pointer `left` forward as long as the current element is less than or equal to the next element.
        # Step 2: If the pointer reaches the end of the array, it means the entire array is already non-decreasing, so no subarray needs to be removed and we return 0.
        # Step 3: If the array is not fully sorted, we then find the longest non-decreasing suffix from the end of the array by moving another pointer `right` backward while the previous element is less than or equal to the current element.
        # Step 4: At this point the array has three parts: a sorted prefix, a middle unsorted part, and a sorted suffix. One simple option is to remove either the whole middle and suffix or the whole prefix and middle, so we initialize the answer with the minimum of those two possibilities.
        # Step 5: Next we try to merge the prefix and suffix more efficiently by using two pointers `i` and `j`. Pointer `i` scans the prefix and pointer `j` scans the suffix starting from `right`.
        # Step 6: If `arr[i]` is less than or equal to `arr[j]`, it means these two parts can connect without breaking the sorted order, so the subarray between them can be removed and we update the result with the smaller removal length.
        # Step 7: If `arr[i]` is greater than `arr[j]`, we move the suffix pointer forward to find a larger value that can maintain the non-decreasing order.

        n = len(arr)

        # Step 1: Find longest non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1

        # Already sorted
        if left == n - 1:
            return 0

        # Step 2: Find longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Remove either prefix or suffix completely
        result = min(n - left - 1, right)

        # Step 3: Try merging prefix and suffix
        i = 0
        j = right

        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result