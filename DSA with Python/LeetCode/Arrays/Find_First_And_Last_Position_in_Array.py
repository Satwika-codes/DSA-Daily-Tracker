# PROBLEM NUMBER: 34
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 34. Find First and Last Position of Element in Sorted Array
# DIFFICULTY: MEDIUM
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Approach:
        # Step 1: Use binary search to find the leftmost (first) occurrence of target.
        # Step 2: Use binary search to find the rightmost (last) occurrence of target.
        # Step 3: Return the indices [leftmost, rightmost]. If target not found, return [-1, -1].

        def findLeft():
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:  # Move left if mid >= target
                    r = mid - 1
                else:
                    l = mid + 1
                if nums[mid] == target:  # Update answer when target found
                    ans = mid
            return ans

        def findRight():
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:  # Move right if mid <= target
                    l = mid + 1
                else:
                    r = mid - 1
                if nums[mid] == target:  # Update answer when target found
                    ans = mid
            return ans

        # Step 3: Return the final range [leftmost, rightmost]
        return [findLeft(), findRight()]
