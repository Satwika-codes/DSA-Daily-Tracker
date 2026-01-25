# PROBLEM NUMBER: 905
# https://leetcode.com/problems/sort-array-by-parity/
# 905. Sort Array By Parity
# DIFFICULTY: EASY
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach:
        # - Use two pointers: `left` starting from the beginning and `right` from the end.
        # - The goal is to place even numbers on the left side and odd numbers on the right side.
        # - While `left` is less than `right`:
        #     1. If the element at `left` is odd and the element at `right` is even,
        #        swap them because they are on the wrong sides.
        #     2. If the element at `left` is even, it is correctly placed → move `left` forward.
        #     3. If the element at `right` is odd, it is correctly placed → move `right` backward.
        # - Continue until both pointers meet.
        # - Return the modified array.

        # Time Complexity: O(n)
        # Space Complexity: O(1)  (in-place)
        

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1

        return nums
