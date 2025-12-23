# PROBLEM NUMBER:1512
# https://leetcode.com/problems/number-of-good-pairs/
# 1512.Number of good pairs
# DIFFICULTY:EASY
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        # APPROACH:
        # - We need to count pairs (i, j) such that i < j and nums[i] == nums[j].
        # - Use a hashmap to store the frequency of each number seen so far.
        # - For every new occurrence of a number, it can form pairs with all
        #   previous occurrences of the same number.
        # - Add the current frequency to the answer, then increment the count.
        count = {}
        pairs = 0

        for num in nums:
            pairs += count.get(num, 0)
            count[num] = count.get(num, 0) + 1

        return pairs
