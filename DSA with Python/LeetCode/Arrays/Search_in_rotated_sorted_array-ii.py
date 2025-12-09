# PROBLEM NUMBER: 81
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# 81.Search in Rotated Sorted Array II
# DIFFICULTY: HARD
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        # Approach:
        # Step 1: This is a rotated sorted array that may contain duplicates.
        #         Because of duplicates, normal binary search rotation logic becomes tricky.
        #
        # Step 2: Perform modified binary search:
        #         • Compute mid.
        #         • If nums[mid] == target → return True.
        #
        # Step 3: Handle duplicates specially:
        #         • If nums[l] == nums[mid] == nums[r], we cannot decide which side is sorted.
        #         • So shrink the search window by doing l += 1 and r -= 1.
        #
        # Step 4: Otherwise decide which half is sorted:
        #         Case A: Left half is sorted (nums[l] <= nums[mid]):
        #                 - If target lies inside this sorted half → move r to mid - 1.
        #                 - Else → search in right half (l = mid + 1).
        #
        #         Case B: Right half is sorted:
        #                 - If target lies inside this sorted half → move l to mid + 1.
        #                 - Else → search left half (r = mid - 1).
        #
        # Step 5: If the loop ends without finding the target → return False.

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True

            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
