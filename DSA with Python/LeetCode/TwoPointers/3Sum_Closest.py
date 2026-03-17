# PROBLEM NUMBER: 16
# https://leetcode.com/problems/3sum-closest/
# 16. 3Sum Closest
# DIFFICULTY: MEDIUM
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Approach:
        # We need to find three numbers in the array whose sum is closest to the given target.
        
        # Step 1: Sort the array so we can efficiently use the two-pointer technique.
        
        # Step 2: Initialize a variable "closest" with the sum of the first three elements.
        #         This will store the best (closest) sum found so far.
        
        # Step 3: Iterate through the array using index i from 0 to n-3.
        #         Treat nums[i] as the first element of the triplet.
        
        # Step 4: Use two pointers for the remaining two elements:
        #         left = i + 1
        #         right = n - 1
        
        # Step 5: Compute the current sum:
        #         curr_sum = nums[i] + nums[left] + nums[right]
        
        # Step 6: If the difference between curr_sum and target is smaller
        #         than the difference between closest and target,
        #         update closest = curr_sum.
        
        # Step 7: Adjust pointers:
        #         • If curr_sum < target → increase left (need a larger sum).
        #         • If curr_sum > target → decrease right (need a smaller sum).
        #         • If curr_sum == target → this is the best possible answer,
        #           so return it immediately.
        
        # Step 8: Continue until all possibilities are explored.
        
        # Step 9: Return the closest sum found.
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum

        return closest
        