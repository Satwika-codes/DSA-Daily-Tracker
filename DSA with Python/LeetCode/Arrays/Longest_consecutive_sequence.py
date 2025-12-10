# PROBLEM NUMBER: 128
# https://leetcode.com/problems/longest-consecutive-sequence/
# 128. Longest Consecutive Sequence
# DIFFICULTY: HARD
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # Step 1: Convert the list into a set for O(1) lookups.
        # Step 2: For each number, check if it is the *start* of a sequence
        #         → i.e., (num - 1) should NOT exist in the set.
        # Step 3: If it's a start, expand forward (num + 1, num + 2, ...)
        #         and count how long the sequence continues.
        # Step 4: Track the maximum sequence length encountered.
        # Step 5: Return the longest consecutive sequence length.

        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:  # start of a sequence
                current = num
                length = 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                max_len = max(max_len, length)

        return max_len
