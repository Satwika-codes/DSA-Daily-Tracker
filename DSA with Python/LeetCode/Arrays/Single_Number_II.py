# PROBLEM NUMBER: 260
# https://leetcode.com/problems/single-number-ii/
# Single Number II
# DIFFICULTY: MEDIUM
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach (Bitmasking with Two Counters):
        #
        # In this problem: 
        #   - Every number appears 3 times except one single number that appears once.
        #   - Goal: return that single unique number.
        #
        # Instead of using extra memory (maps/arrays),
        # we use bit manipulation with two variables:
        #
        #   ones → stores bits that have appeared exactly once so far.
        #   twos → stores bits that have appeared exactly twice so far.
        #
        # Logic:
        # • For each number:
        #       ones = (ones XOR num) AND NOT(twos)
        #           → add num’s bits to ones, but remove bits already counted in twos
        #
        #       twos = (twos XOR num) AND NOT(ones)
        #           → add num’s bits to twos, but remove bits newly added to ones
        #
        # After processing all numbers:
        #   - Bits that appear 3 times automatically get removed.
        #   - Bits that appear once remain only in 'ones'.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        #
        # Result is stored in 'ones'.

        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones
