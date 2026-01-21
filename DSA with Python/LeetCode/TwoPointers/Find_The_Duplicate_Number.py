# PROBLEM NUMBER: 287
# https://leetcode.com/problems/find-the-duplicate-number/
# 287. Find the Duplicate Number
# DIFFICULTY: MEDIUM
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Approach:
        # Treat the array as a linked list where each index points to nums[index].
        # Since there is exactly one duplicate number, a cycle must exist.

        # Use Floyd’s Tortoise and Hare algorithm:
        # 1) Move slow pointer by 1 step and fast pointer by 2 steps until they meet.
        # 2) Reset one pointer to the start and move both by 1 step.
        # 3) The point where they meet again is the duplicate number.
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
