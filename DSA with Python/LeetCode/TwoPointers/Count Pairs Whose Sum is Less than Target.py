# PROBLEM NUMBER: 2824
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
# 2824. Count Pairs Whose Sum is Less than Target
# DIFFICULTY: MEDIUM
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Approach:
        # We need to count pairs (i, j) such that:
        #   i < j
        #   nums[i] + nums[j] < target
        
        # Step 1: Sort the array so we can use the two-pointer technique.
        # Step 2: Use two pointers:
        #         left  → start of array
        #         right → end of array
        # Step 3: If nums[left] + nums[right] < target:
        #         then ALL pairs (left, left+1 ... right) with nums[left]
        #         will also satisfy the condition because the array is sorted.
        #         So we add (right - left) pairs.
        # Step 4: Move left pointer forward to check next element.
        # Step 5: If the sum ≥ target, move right pointer backward to reduce the sum.
        # Step 6: Continue until left >= right.

        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left)
                left += 1
            else:
                right -= 1

        return count