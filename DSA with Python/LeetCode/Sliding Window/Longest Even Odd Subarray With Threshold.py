# PROBLEM NUMBER: 2760
# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/
# Longest Even Odd Subarray With Threshold
# DIFFICULTY: EASY
class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        # Approach:
        # We need to find the longest subarray where:
        # • The first element is even and ≤ threshold
        # • Elements alternate between even and odd
        # • Every element is ≤ threshold
        #
        # Step 1: Iterate through each index i as a potential starting point.
        #
        # Step 2: Check if nums[i] is a valid start:
        #         • It must be even
        #         • It must be ≤ threshold
        #         If not, skip this index.
        #
        # Step 3: Initialize length = 1 and set prev = nums[i].
        #
        # Step 4: Expand the subarray from index i:
        #         For each next element nums[j]:
        #         • If nums[j] > threshold → break (invalid element)
        #         • If nums[j] has same parity as prev → break (not alternating)
        #
        # Step 5: If valid, increase length and update prev.
        #
        # Step 6: After finishing expansion for this starting point,
        #         update max_len with the maximum length found.
        #
        # Step 7: Continue for all starting indices and return max_len.

        n = len(nums)
        max_len = 0

        for i in range(n):
            # must start with even and ≤ threshold
            if nums[i] % 2 != 0 or nums[i] > threshold:
                continue

            length = 1
            prev = nums[i]

            for j in range(i + 1, n):
                if nums[j] > threshold:
                    break

                # check alternating parity
                if nums[j] % 2 == prev % 2:
                    break

                length += 1
                prev = nums[j]

            max_len = max(max_len, length)

        return max_len