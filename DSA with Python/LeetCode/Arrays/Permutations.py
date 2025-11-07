# PROBLEM NUMBER: 46
# https://leetcode.com/problems/permutations/
# 46. Permutations
# DIFFICULTY: MEDIUM
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # - Use **Backtracking** to generate all possible permutations.
        # - Maintain two lists:
        #   • `path`: current permutation being built.  
        #   • `remaining`: elements yet to be added.
        # - At each recursive call:
        #   • If no elements remain, add the completed path to results.
        #   • Otherwise, for each element in remaining:
        #       - Choose it, append to path, and recurse with remaining elements excluding it.
        # - Continue exploring all possible choices.
        # - Return all collected permutations.
        # Time: O(n!)  |  Space: O(n) (recursion depth)
        res = []
        def backtrack(path, remaining):
            if not remaining:
                res.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        backtrack([], nums)
        return res