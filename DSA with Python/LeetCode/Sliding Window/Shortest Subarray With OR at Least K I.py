# PROBLEM NUMBER: 3095
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k
# Shortest Subarray With OR at Least K
# DIFFICULTY:EASY
class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Approach:
        # We need to find the minimum length subarray such that
        # bitwise OR of its elements is ≥ k.
        #
        # Step 1: Use sliding window with two pointers (left, right).
        #
        # Step 2: Maintain an array bit_count[0..31] where:
        #         bit_count[i] = number of elements in current window
        #         having i-th bit set.
        #
        # Step 3: Define a helper function get_or():
        #         • If bit_count[i] > 0 → i-th bit is set in OR result
        #         • Construct OR using these bits
        #
        # Step 4: Expand window by moving 'right':
        #         • For nums[right], update bit_count accordingly
        #
        # Step 5: While current OR ≥ k:
        #         • Update result with current window length
        #         • Shrink window from left:
        #             - Remove nums[left] from bit_count
        #             - Move left forward
        #
        # Step 6: Continue until all elements are processed.
        #
        # Step 7: If no valid subarray found, return -1,
        #         else return minimum length found.

        n = len(nums)
        bit_count = [0] * 32

        def get_or():
            res = 0
            for i in range(32):
                if bit_count[i] > 0:
                    res |= (1 << i)
            return res

        left = 0
        res = float('inf')

        for right in range(n):
            # add nums[right]
            for i in range(32):
                if nums[right] & (1 << i):
                    bit_count[i] += 1

            # shrink window
            while left <= right and get_or() >= k:
                res = min(res, right - left + 1)

                for i in range(32):
                    if nums[left] & (1 << i):
                        bit_count[i] -= 1

                left += 1

        return res if res != float('inf') else -1