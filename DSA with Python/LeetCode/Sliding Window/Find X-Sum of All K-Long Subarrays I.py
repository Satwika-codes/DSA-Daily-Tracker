# PROBLEM NUMBER: 1007
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays/
# 3318. Find X-Sum of All K-Long Subarrays
# DIFFICULTY: EASY
from collections import Counter

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        # Approach:
        # For each subarray (window) of size k, we need to:
        # • Count frequency of elements
        # • Pick top x elements based on:
        #     1. Higher frequency first
        #     2. If tie → larger value first
        # • Compute sum = value * frequency for those x elements
        #
        # Step 1: Iterate over all windows of size k.
        #
        # Step 2: For each window:
        #         • Use Counter to count frequency of elements.
        #
        # Step 3: Sort the (value, frequency) pairs:
        #         • Primary key: frequency (descending)
        #         • Secondary key: value (descending)
        #
        # Step 4: Take first x elements from sorted list.
        #
        # Step 5: For each selected (value, count),
        #         add (value * count) to total.
        #
        # Step 6: Append total to result list.
        #
        # Step 7: Return result.

        n = len(nums)
        result = []

        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)

            # sort by frequency desc, value desc
            sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))

            total = 0
            for j in range(min(x, len(sorted_items))):
                val, count = sorted_items[j]
                total += val * count

            result.append(total)

        return result

















