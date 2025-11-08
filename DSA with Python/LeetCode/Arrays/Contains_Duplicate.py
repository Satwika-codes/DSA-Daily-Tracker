# PROBLEM NUMBER: 217
# https://leetcode.com/problems/contains-duplicate/
# 217. Contains Duplicate
# DIFFICULTY: EASY
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach:
        # - Goal: Check if any number appears more than once in the list.
        # - Use a **set** to automatically remove duplicates.
        # - Compare lengths:
        #     • If length of `nums` ≠ length of `set(nums)`, duplicates exist → return True.
        #     • Else, all elements are unique → return False.
        # - Time Complexity: O(n)
        # - Space Complexity: O(n)
        return len(nums) != len(set(nums))