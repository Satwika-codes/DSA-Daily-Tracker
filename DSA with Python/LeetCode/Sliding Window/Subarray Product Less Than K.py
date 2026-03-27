# PROBLEM NUMBER: 713
# https://leetcode.com/problems/subarray-product-less-than-k/
# Subarray Product Less Than K
# DIFFICULTY:MEDIUM
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Approach:
        # We need to count the number of contiguous subarrays
        # whose product is strictly less than k.
        #
        # Step 1: Handle edge case:
        #         • If k <= 1, no valid subarray exists → return 0
        #
        # Step 2: Use sliding window technique with two pointers:
        #         • left → start of window
        #         • right → end of window
        #
        # Step 3: Maintain a variable 'prod' to store product
        #         of current window.
        #
        # Step 4: Expand window by multiplying nums[right] to prod.
        #
        # Step 5: If prod >= k:
        #         • Shrink window from left
        #         • Divide prod by nums[left]
        #         • Move left forward
        #
        # Step 6: Once prod < k:
        #         • All subarrays ending at 'right' are valid
        #         • Number of such subarrays = (right - left + 1)
        #
        # Step 7: Add this count to total count.
        #
        # Step 8: Continue until all elements are processed.
        #
        # Step 9: Return the total count.

        if k <= 1:
            return 0

        prod = 1
        left = 0
        count = 0

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k:
                prod //= nums[left]
                left += 1

            count += (right - left + 1)

        return count