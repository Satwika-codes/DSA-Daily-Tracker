# PROBLEM NUMBER: 35
# https://leetcode.com/problems/search-insert-position/
# 35. Search Insert Position
# DIFFICULTY: EASY
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Approach:
        # - Use **binary search** to find the correct index where the target should be inserted.  
        # - Initialize `left = 0` and `right = len(nums) - 1`.  
        # - While `left <= right`:
        #   • Compute `mid = (left + right) // 2`.  
        #   • If `nums[mid] == target`, return `mid` (found exact match).  
        #   • If `nums[mid] < target`, move search space to the right half (`left = mid + 1`).  
        #   • Else, move to the left half (`right = mid - 1`).  
        # - If target is not found, `left` will be the position where it should be inserted.  
        # - Return `left`.
        # Time: O(log n)  |  Space: O(1)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
        