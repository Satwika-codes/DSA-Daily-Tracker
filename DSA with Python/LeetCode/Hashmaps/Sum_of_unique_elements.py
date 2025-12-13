# PROBLEM NUMBER: 1748
# https://leetcode.com/problems/sum-of-unique-elements
# 1748. Sum of Unique Elements
# DIFFICULTY: EASY
from collections import Counter
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #  APPROACH 
        # Step 1: Count the frequency of each number in the array using Counter.
        # Step 2: A number is considered "unique" if its frequency is exactly 1.
        #
        # Step 3: Iterate through all numbers and their frequencies.
        #         - Select only the numbers with frequency == 1.
        # Step 4: Sum all the unique numbers.
        #
        # Step 5: Return the total sum of unique numbers.

        counts = Counter(nums)
        return sum(num for num, freq in counts.items() if freq == 1)
