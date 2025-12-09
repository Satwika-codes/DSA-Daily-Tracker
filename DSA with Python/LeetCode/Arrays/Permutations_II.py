# PROBLEM NUMBER: 47
# https://leetcode.com/problems/permutations-ii/
# 47. Permutations II
# DIFFICULTY: MEDIUM
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Approach:
        # Step 1: Sort the array so duplicates become adjacent. 
        #         This helps us skip generating the same permutation multiple times.
        #
        # Step 2: Use backtracking to build permutations:
        #         • Maintain a 'used' array to track which elements are already taken.
        #
        # Step 3: At each position, try choosing nums[i] if:
        #         • It is not already used, and
        #         • It is not a duplicate in the same position:
        #             (i > 0 and nums[i] == nums[i-1] and used[i-1] == False)
        #           This ensures we only pick the first unused duplicate in each layer.
        #
        # Step 4: Add the chosen number to the current path, recurse, 
        #         then backtrack by removing it and marking it unused again.
        #
        # Step 5: When path length equals array length, record it as a valid unique permutation.

        nums.sort()
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])
        return res
