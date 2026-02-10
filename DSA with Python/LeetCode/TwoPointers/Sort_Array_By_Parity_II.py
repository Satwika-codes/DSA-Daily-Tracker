# PROBLEM NUMBER: 922
# https://leetcode.com/problems/sort-array-by-parity-ii/description/
# 922. Sort Array By Parity
# DIFFICULTY: MEDIUM
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach:
        # We are given an array where:
        # - Half of the elements are even
        # - Half of the elements are odd

        # Goal:
        # - Place even numbers at even indices
        # - Place odd numbers at odd indices

        # Steps:
        # 1. Use two pointers:
        #    - `even` starts at index 0
        #    - `odd` starts at index 1

        # 2. Traverse the array:
        #    - If nums[even] is even → move `even` by 2
        #    - If nums[odd] is odd → move `odd` by 2
        #    - Otherwise, swap nums[even] and nums[odd]

        # 3. Continue until both pointers are within bounds.

        # Time Complexity:
        # O(n)

        # Space Complexity:
        # O(1)  (in-place)

        even = 0
        odd = 1
        n = len(nums)

        while even < n and odd < n:
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 == 1:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]

        return nums
