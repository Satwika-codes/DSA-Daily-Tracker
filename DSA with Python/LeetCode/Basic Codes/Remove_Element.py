# PROBLEM NUMBER: 27
# https://leetcode.com/problems/remove-element/
# DIFFICULTY: Easy
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        # APPROACH:
        # This solution removes all occurrences of a given value `val` from the list `nums`.
        # 1. Check if the list `nums` is empty; if so, return 0.
        # 2. Use a while loop to repeatedly check if `val` exists in `nums`:
        #    - If it exists, remove one occurrence of `val` using `nums.remove(val)`.
        # 3. Continue the loop until all occurrences of `val` are removed.
        # 4. Return the length of the modified list, which represents the number of remaining elements.
        # This approach provides a straightforward method to remove elements, though it may not be the most efficient for very large lists.

        """
        count=0
        if (len(nums)==0):
            return 0
        while val in nums:
            nums.remove(val)
        return len(nums)