# PROBLEM NUMBER: 1004
# https://leetcode.com/problems/max-consecutive-ones-iii/
# Max Consecutive Ones III
# DIFFICULTY: MEDIUM
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Approach:
        # We need to find the longest subarray containing 1s
        # after flipping at most k zeros.
        #
        # Step 1: Use sliding window with two pointers:
        #         • left → start of window
        #         • right → end of window
        #
        # Step 2: Keep track of number of zeros in current window.
        #
        # Step 3: Expand window by moving right pointer:
        #         • If nums[right] == 0 → increment zeros count
        #
        # Step 4: If zeros exceed k:
        #         • Shrink window from left
        #         • If nums[left] == 0 → decrement zeros count
        #         • Move left forward
        #
        # Step 5: At every step, window has at most k zeros:
        #         • Update max_len with current window size
        #
        # Step 6: Return the maximum length found

        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # shrink window if invalid
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len