# PROBLEM NUMBER: 2381
# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/
# Minimum Adjacent Swaps for K Consecutive Ones
# DIFFICULTY: HARD
class Solution(object):
    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Approach:
        # We need to group k ones together with minimum moves.
        # Each move shifts a '1' to an adjacent position.
        #
        # Step 1: Collect indices of all 1s in the array.
        #
        # Step 2: Adjust positions to remove gaps effect:
        #         • For each index i in pos:
        #           pos[i] = pos[i] - i
        #         This simplifies movement calculation.
        #
        # Step 3: Build prefix sum array of pos for fast range sum queries.
        #
        # Step 4: Use sliding window of size k over pos array.
        #
        # Step 5: For each window:
        #         • Find median position (optimal target)
        #
        # Step 6: Calculate cost:
        #         • Left side cost:
        #           median * count_left - sum_left
        #
        #         • Right side cost:
        #           sum_right - median * count_right
        #
        # Step 7: Total cost = left_cost + right_cost
        #
        # Step 8: Track minimum cost across all windows.
        #
        # Step 9: Return the minimum moves required.

        # Step 1: positions of 1s
        pos = []
        for i, num in enumerate(nums):
            if num == 1:
                pos.append(i)

        # Step 2: adjust positions (remove gaps effect)
        for i in range(len(pos)):
            pos[i] -= i

        # Step 3: prefix sum
        prefix = [0]
        for p in pos:
            prefix.append(prefix[-1] + p)

        res = float('inf')

        # Step 4: sliding window of size k
        for i in range(len(pos) - k + 1):
            mid = i + k // 2
            median = pos[mid]

            left_cost = median * (mid - i) - (prefix[mid] - prefix[i])
            right_cost = (prefix[i + k] - prefix[mid + 1]) - median * (i + k - mid - 1)

            res = min(res, left_cost + right_cost)

        return res