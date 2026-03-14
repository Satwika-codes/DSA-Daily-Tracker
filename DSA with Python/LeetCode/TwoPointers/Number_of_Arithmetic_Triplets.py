# PROBLEM NUMBER: 2367
# https://leetcode.com/problems/number-of-arithmetic-triplets/
# 2367. Number of Arithmetic Triplets
# DIFFICULTY: EASY
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        # Approach:
        # Step 1: The task is to count arithmetic triplets (x, x + diff, x + 2*diff) where all three numbers exist in the array and maintain the required difference pattern.
        # Step 2: Convert the list `nums` into a set to allow constant time O(1) lookups when checking if specific numbers exist in the array.
        # Step 3: Initialize a counter variable to keep track of how many valid arithmetic triplets are found.
        # Step 4: Iterate through each number `x` in the original list `nums`, treating it as the potential starting element of a triplet.
        # Step 5: For each `x`, check whether `x + diff` exists in the set and also whether `x + 2 * diff` exists in the set.
        # Step 6: If both values exist, then the sequence (x, x + diff, x + 2*diff) forms a valid arithmetic triplet, so increment the counter.
        # Step 7: Continue this process for every element in the list to check all possible starting points.
        # Step 8: After the iteration is complete, return the final count representing the number of valid arithmetic triplets found.
        num_set = set(nums)
        count = 0

        for x in nums:
            if x + diff in num_set and x + 2 * diff in num_set:
                count += 1

        return count