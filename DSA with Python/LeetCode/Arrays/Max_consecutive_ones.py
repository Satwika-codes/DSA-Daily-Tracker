# PROBLEM NUMBER: 485
# https://leetcode.com/problems/max-consecutive-ones/
# 485. Max Consecutive Ones
# DIFFICULTY: EASY
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # Step 1: Traverse the array and keep a running count of consecutive 1s.
        # Step 2: Every time we see a 1, increase the count and update max_count.
        # Step 3: When we see a 0, reset the count to 0 (sequence breaks).
        # Step 4: The maximum count reached at any point is the answer.

        max_count = 0
        count = 0
        
        for x in nums:
            if x == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        
        return max_count