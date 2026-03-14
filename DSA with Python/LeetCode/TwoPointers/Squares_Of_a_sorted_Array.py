# https://leetcode.com/problems/squares-of-a-sorted-array/
# PROBLEM NUMBER: 977
# 977. Squares of a Sorted Array
# DIFFICULTY: EASY
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach:
        # Step 1: The array `nums` is already sorted in non-decreasing order, but it may contain negative numbers whose squares can become larger than positive numbers, so we cannot simply square and keep the same order.
        # Step 2: To efficiently produce a sorted array of squares, use a two-pointer approach where `left` starts at the beginning of the array and `right` starts at the end.
        # Step 3: Create a result array of the same size as `nums` to store the squared values in sorted order.
        # Step 4: Since the largest square will always come from either the most negative number (left side) or the largest positive number (right side), compare the squares of `nums[left]` and `nums[right]`.
        # Step 5: Place the larger of the two squared values at the current position `pos` in the result array, which starts from the end because we are filling the largest values first.
        # Step 6: If the square from the left pointer is larger, store it in the result and move the left pointer forward; otherwise store the right square and move the right pointer backward.
        # Step 7: After placing the value, move the `pos` pointer one step backward to fill the next largest square.
        # Step 8: Continue this process until the two pointers cross each other, ensuring all squared values are placed in sorted order.
        # Step 9: Finally return the result array which now contains the squares of all elements from `nums` arranged in non-decreasing order.

        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1

            pos -= 1

        return result