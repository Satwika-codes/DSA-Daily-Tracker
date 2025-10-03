# 136. Single Number
# https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        """
        Find the element that appears only once in the list.

        :type nums: List[int]
        :rtype: int

        Approach:
        - Loop through each number in the list.
        - Count how many times it appears using nums.count().
        - If it appears only once, return it immediately.

        Note:
        - This works for all test cases.
        - Time Complexity: O(n^2) because count() scans the list for each element.
        - Space Complexity: O(1)
        """

        for i in nums:
            count = nums.count(i)  # Count occurrences of i in the list
            if count == 1:         # If it appears only once
                return i           # Return it immediately
            # Otherwise continue to next number

