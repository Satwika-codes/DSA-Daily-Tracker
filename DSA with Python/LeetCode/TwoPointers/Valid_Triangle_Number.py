# PROBLEM NUMBER: 611
# https://leetcode.com/problems/valid-triangle-number/
# 611.Valid Triangle Number
# DIFFICULTY: MEDIUM
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # 1. Sort the array.
        # 2. Fix the largest side at index k.
        # 3. Use two pointers:
        #    - left = 0
        #    - right = k - 1
        # 4. If nums[left] + nums[right] > nums[k],
        #    then all values between left and right
        #    form valid triangles with nums[k].
        #    Add (right - left) to count.
        #    Decrease right.
        # 5. Otherwise, increase left.
        # Time Complexity: O(n²)
        # Space Complexity: O(1)

        nums.sort()
        n = len(nums)
        count = 0

        for k in range(n - 1, 1, -1):
            left = 0
            right = k - 1

            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count
