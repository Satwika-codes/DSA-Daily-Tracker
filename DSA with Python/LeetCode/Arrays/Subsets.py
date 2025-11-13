# PROBLEM NUMBER: 78
# https://leetcode.com/problems/subsets/
# 78.Subsets
# DIFFICULTY: MEDIUM
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """# APPROACH (Backtracking):
        # 1. We use backtracking to generate all possible subsets (the power set).
        # 2. Start from index 0 with an empty path (current subset).
        # 3. At each step, add the current subset (path) to the result list.
        # 4. Iterate through remaining elements, include each element, 
        #    recursively build further subsets, then backtrack by removing the element.
        # Example:
        # nums = [1, 2, 3]
        # Subsets formed:
        # [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]
        # Time Complexity: O(2^n) — each element can be either included or excluded.
        # Space Complexity: O(n) — recursion stack depth (excluding output storage).
        res = []
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res
