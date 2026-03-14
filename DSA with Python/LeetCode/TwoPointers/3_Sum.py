# PROBLEM NUMBER: 15
# https://leetcode.com/problems/3sum/
# 15. 3Sum
# DIFFICULTY: MEDIUM
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Approach:
        # Step 1: The goal is to find all unique triplets in the array whose sum equals zero, so first sort the array to make it easier to apply the two-pointer technique and handle duplicates.
        # Step 2: Initialize an empty list `result` to store all valid triplets and get the length of the array.
        # Step 3: Iterate through the array using index `i`, treating `nums[i]` as the first element of the potential triplet.
        # Step 4: To avoid duplicate triplets, skip the current index if it has the same value as the previous element.
        # Step 5: For each fixed element `nums[i]`, initialize two pointers: `left` starting at `i + 1` and `right` starting at the end of the array.
        # Step 6: Calculate the sum of the three elements `nums[i] + nums[left] + nums[right]`.
        # Step 7: If the sum equals zero, a valid triplet is found, so append it to the result list.
        # Step 8: After finding a valid triplet, skip duplicate values for both `left` and `right` pointers to ensure only unique triplets are added.
        # Step 9: Move both pointers inward (`left += 1` and `right -= 1`) to search for new combinations.
        # Step 10: If the total sum is less than zero, move the `left` pointer forward to increase the sum since the array is sorted.
        # Step 11: If the total sum is greater than zero, move the `right` pointer backward to decrease the sum.
        # Step 12: Continue this process until the `left` pointer meets the `right` pointer, then move to the next value of `i`.
        # Step 13: Finally return the list of all unique triplets whose sum is zero.
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result