# PROBLEM NUMBER: 80
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# 80. Remove Duplicates from Sorted Array II
# DIFFICULTY: MEDIUM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # ----------------------------------------------------------
        # We are allowed to keep each number at most **twice**.
        #
        # Key Idea:
        # Use a pointer `k` which tracks the position where the next
        # valid element should go.
        #
        # Steps:
        # 1. If array length ≤ 2, it's already valid → return length.
        # 2. Start `k = 2` because first two elements are always allowed.
        # 3. Loop from index 2 onwards:
        #       - Compare nums[i] with nums[k-2].
        #       - If different → it's allowed to keep.
        #         Place nums[i] at nums[k] and increment `k`.
        #       - If same → skip (more than two duplicates).
        #
        # 4. Return k → the new length of the array with allowed duplicates.

        if len(nums) <= 2:
            return len(nums)
        
        k = 2  # first two numbers are always kept

        for i in range(2, len(nums)):
            # If current number is not equal to the element two positions behind,
            # it means we haven't yet stored it twice → keep it.
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
