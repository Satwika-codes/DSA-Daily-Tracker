# PROBLEM NUMBER: 1660
# https://leetcode.com/problems/maximum-subarray-with-equal-products/
# Maximum Subarray With Equal Products
# DIFFICULTY: EASY
from fractions import gcd

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # We need to find the maximum length subarray such that:
        # product of elements == (gcd of elements) * (lcm of elements)
        #
        # Step 1: Iterate over all possible starting indices i.
        #
        # Step 2: Initialize three values for the subarray starting at i:
        #         • prod → product of elements
        #         • g    → gcd of elements
        #         • l    → lcm of elements
        #
        # Step 3: Extend the subarray by moving index j from i to n-1.
        #
        # Step 4: For each new element nums[j]:
        #         • Update product: prod *= nums[j]
        #         • Update gcd: g = gcd(g, nums[j])
        #         • Update lcm using formula:
        #               lcm(a, b) = (a * b) // gcd(a, b)
        #
        # Step 5: Check if the condition holds:
        #         prod == g * l
        #         If yes, update max_len with the current subarray length.
        #
        # Step 6: If prod becomes greater than g * l,
        #         break early since the condition won't be satisfied further.
        #
        # Step 7: Continue checking all subarrays and return max_len.

        n = len(nums)
        max_len = 1

        for i in range(n):
            prod = nums[i]
            g = nums[i]
            l = nums[i]

            for j in range(i, n):
                if j > i:
                    prod *= nums[j]
                    g = gcd(g, nums[j])
                    l = (l * nums[j]) // gcd(l, nums[j])

                if prod == g * l:
                    max_len = max(max_len, j - i + 1)

                if prod > g * l:
                    break

        return max_len