# PROBLEM NUMBER: 2465
# https://leetcode.com/problems/number-of-distinct-averages/description/
# 2465. Number of Distinct Averages
# DIFFICULTY: EASY
class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # Step 1: The goal is to repeatedly take the smallest and largest numbers from the array, compute their average, and count how many distinct averages appear.
        # Step 2: First sort the array so that the smallest elements are at the beginning and the largest elements are at the end.
        # Step 3: Use two pointers: `left` starting from the beginning of the array and `right` starting from the end.
        # Step 4: Create a set `seen` to store the unique averages encountered during the process.
        # Step 5: While `left` is less than `right`, compute the sum of the elements at these positions.
        # Step 6: Instead of storing the average directly, store the sum in the set because the average is simply the sum divided by 2 and distinct sums correspond to distinct averages.
        # Step 7: Add this sum to the `seen` set so duplicates are automatically ignored.
        # Step 8: Move the `left` pointer one step forward and the `right` pointer one step backward to process the next smallest and largest pair.
        # Step 9: Continue this process until the pointers meet.
        # Step 10: Finally return the size of the `seen` set, which represents the number of distinct averages formed.

        nums.sort()

        left = 0
        right = len(nums) - 1

        seen = set()

        while left < right:
            total = nums[left] + nums[right]
            seen.add(total)   # store sum instead of average

            left += 1
            right -= 1

        return len(seen)