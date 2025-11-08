# PROBLEM NUMBER:39
# https://leetcode.com/problems/combination-sum/
# 39. Combination Sum
# DIFFICULTY:MEDIUM
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Approach:
        # - Problem: Find all unique combinations of numbers from `candidates` that sum up to `target`.
        # - Use **backtracking** to explore all possible combinations.
        # - Parameters:
        #     • `start` → ensures we don’t reuse previous elements (avoids duplicates in different orders).  
        #     • `path` → current combination.  
        #     • `total` → current sum of elements in `path`.
        # - Base cases:
        #     • If `total == target`, store a copy of `path` in the result.  
        #     • If `total > target`, stop exploring this path.
        # - Recursive step:
        #     • Loop from `start` to end, pick an element, and call `backtrack` with updated sum and same index (since repetition allowed).
        # - After recursion, remove last element (backtrack).
        # Time: O(2^n) in worst case | Space: O(target)
        res = []
        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return res