# PROBLEM NUMBER: 189
# https://leetcode.com/problems/rotate-array/
# 189. Rotate Array
# DIFFICULTY: MEDIUM
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Approach (Reverse Method):
        #
        # Goal:
        # Rotate the array to the right by k steps, in-place.
        #
        # Steps:
        # 1. Take k = k % n (because rotating n times gives the same array).
        #
        # 2. Reverse the entire array.
        #       Example: [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
        #
        # 3. Reverse the first k elements.
        #       Example: k=3 → reverse [7,6,5] -> [5,6,7]
        #
        # 4. Reverse the remaining n-k elements.
        #       Example: reverse [4,3,2,1] -> [1,2,3,4]
        #
        # Final array = [5,6,7,1,2,3,4]
        #
        # This method gives O(n) time and O(1) extra space.

        n = len(nums)
        k %= n
        
        def rev(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        rev(0, n - 1)      # Step 2: Reverse full array
        rev(0, k - 1)      # Step 3: Reverse first k elements
        rev(k, n - 1)      # Step 4: Reverse the rest
