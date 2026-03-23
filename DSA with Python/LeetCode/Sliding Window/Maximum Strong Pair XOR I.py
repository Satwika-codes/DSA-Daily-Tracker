# PROBLEM NUMBER: 2932
# https://leetcode.com/problems/maximum-strong-pair-xor/
# Maximum Strong Pair XOR
# DIFFICULTY: EASY
class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # We need to find the maximum XOR value among all "strong pairs".
        # A pair (i, j) is strong if:
        #     |nums[i] - nums[j]| <= min(nums[i], nums[j])
        #
        # Step 1: Initialize max_xor = 0 to track the maximum XOR value.
        #
        # Step 2: Use two nested loops to check all possible pairs (i, j).
        #
        # Step 3: For each pair:
        #         • Check if it satisfies the strong pair condition:
        #           abs(nums[i] - nums[j]) <= min(nums[i], nums[j])
        #
        # Step 4: If valid, compute XOR:
        #         nums[i] ^ nums[j]
        #
        # Step 5: Update max_xor if this XOR value is greater.
        #
        # Step 6: After checking all pairs, return max_xor.

        n = len(nums)
        max_xor = 0

        for i in range(n):
            for j in range(n):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    max_xor = max(max_xor, nums[i] ^ nums[j])

        return max_xor