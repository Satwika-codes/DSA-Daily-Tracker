# PROBLEM NUMBER: 665
# https://leetcode.com/problems/non-decreasing-array/
# 665. Non-decreasing Array
# DIFFICULTY: MEDIUM
class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach:
        # Step 1: We are allowed to remove at most one element to make the array strictly increasing.
        # Step 2: Traverse the array and detect the first place where nums[i] <= nums[i-1].
        # Step 3: If such a violation happens again, return False (because more than one removal needed).
        # Step 4: When a violation is found:
        #         - Mark that one element has been removed.
        #         - Decide which element to adjust:
        #             • If nums[i] <= nums[i-2], removing nums[i-1] is safer → set nums[i] = nums[i-1].
        #             • Otherwise removing nums[i] is safe, so do nothing.
        # Step 5: If traversal finishes with ≤1 violation handled, return True.

        removed = False

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if removed:
                    return False
                removed = True

                if i > 1 and nums[i] <= nums[i - 2]:
                    nums[i] = nums[i - 1]

        return True
