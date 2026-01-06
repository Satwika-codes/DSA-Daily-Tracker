# PROBLEM NUMBER: 740
# https://leetcode.com/problems/delete-and-earn/
# 740. Delete and Earn
# DIFFICULTY: MEDIUM
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # This problem can be reduced to the classic "House Robber" problem.

        # When we take a number x, we earn x * frequency[x] points, but we
        # cannot take x-1 or x+1. This is equivalent to robbing houses where
        # adjacent houses cannot both be robbed.

        # Steps:
        # 1. Count total points for each number.
        # 2. Sort the unique numbers.
        # 3. Use dynamic programming where:
        #    - dp_take = max points if we take current number
        #    - dp_skip = max points if we skip current number
        # 4. If current number is consecutive to previous, taking it
        #    depends on skipping the previous one.
        #    Otherwise, we can safely add it to the maximum so far.

        # This ensures optimal result in O(n log n) time.
    

        from collections import Counter

        count = Counter(nums)
        nums_sorted = sorted(count)

        prev = None
        take = skip = 0

        for num in nums_sorted:
            curr_points = num * count[num]

            if prev is not None and num == prev + 1:
                new_take = skip + curr_points
                new_skip = max(skip, take)
            else:
                new_take = max(skip, take) + curr_points
                new_skip = max(skip, take)

            take, skip = new_take, new_skip
            prev = num

        return max(take, skip)
