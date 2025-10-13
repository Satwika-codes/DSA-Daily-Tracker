# PROBLEM NUMBER:18
# https://leetcode.com/problems/4sum/
# 18.4Sum
# DIFFICULTY:MEDIUM
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # APPROACH:
        # This solution finds all unique quadruplets in `nums` that sum up to the given `target`
        # using sorting and a two-pointer technique.
        # 1. Sort the input array `nums` to simplify duplicate handling and allow the use of two pointers.
        # 2. Fix two numbers using nested loops:
        #    - The first loop runs for index `i` from 0 to n-4.
        #    - The second loop runs for index `j` from i+1 to n-3.
        #    - Skip duplicate values for both `i` and `j` to avoid repeating quadruplets.
        # 3. Use two pointers `l` (left) and `r` (right) to find the remaining two numbers:
        #    - Calculate the sum `s = nums[i] + nums[j] + nums[l] + nums[r]`.
        #    - If `s == target`, add the quadruplet to the result list and move both pointers while skipping duplicates.
        #    - If `s < target`, move the left pointer `l` to increase the sum.
        #    - If `s > target`, move the right pointer `r` to decrease the sum.
        # 4. Continue until all combinations are checked and return the result list `res`.
        # Time Complexity: O(n³) — due to the two nested loops and two-pointer traversal.
        # Space Complexity: O(1) — excluding the space used for the result list.
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res

        