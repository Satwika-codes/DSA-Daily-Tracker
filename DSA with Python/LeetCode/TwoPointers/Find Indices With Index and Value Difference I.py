# PROBLEM NUMBER: 2903
# https://leetcode.com/problems/find-indices-with-index-and-value-difference/
# 2903. Find Indices With Index and Value Difference
# DIFFICULTY: EASY

class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        # Approach:
        # Step 1: The goal is to find two indices (i, j) such that the distance between them satisfies j - i >= indexDifference and the absolute difference of their values is at least valueDifference.
        # Step 2: Traverse the array starting from index `indexDifference` so that for every `j`, there exists at least one valid `i = j - indexDifference`.
        # Step 3: Maintain two indices `min_idx` and `max_idx` which track the positions of the smallest and largest values among all valid candidate indices `i`.
        # Step 4: For each step, compute the new candidate index `i = j - indexDifference` and update `min_idx` if `nums[i]` is smaller than the current minimum value.
        # Step 5: Similarly update `max_idx` if `nums[i]` is larger than the current maximum value.
        # Step 6: Once the candidate indices are updated, check whether the absolute difference between `nums[j]` and `nums[min_idx]` is at least `valueDifference`.
        # Step 7: If this condition is satisfied, return the pair `[min_idx, j]` as a valid solution.
        # Step 8: Also check whether the absolute difference between `nums[j]` and `nums[max_idx]` is at least `valueDifference`.
        # Step 9: If this condition holds, return `[max_idx, j]` as another valid solution.
        # Step 10: Continue scanning through the array until a valid pair is found.
        # Step 11: If the loop finishes without finding any valid pair, return `[-1, -1]` to indicate that no such indices exist.

        n = len(nums)
        min_idx = 0
        max_idx = 0

        # Traverse array starting from indexDifference
        for j in range(indexDifference, n):
            i = j - indexDifference

            # Update min and max among valid i candidates
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

            # Check value difference condition
            if abs(nums[j] - nums[min_idx]) >= valueDifference:
                return [min_idx, j]

            if abs(nums[j] - nums[max_idx]) >= valueDifference:
                return [max_idx, j]

        # If no valid pair is found
        return [-1, -1]