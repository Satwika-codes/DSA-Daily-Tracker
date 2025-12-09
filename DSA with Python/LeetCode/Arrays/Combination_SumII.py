# PROBLEM NUMBER: 40
# https://leetcode.com/problems/combination-sum-ii/
# 40. Combination Sum II
# DIFFICULTY: MEDIUM
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Approach:
        # Problem: Find all unique combinations where numbers sum to target.
        # Each number can be used at most once.
        # Key Ideas:
        # 1. Sort the list so duplicates sit together.
        # 2. Use backtracking to explore choices.
        #
        # Steps:
        # 1. Sort the candidates (required to handle duplicates).
        # 2. At each position:
        #      - Skip duplicates: if candidates[i] == candidates[i-1] (same level).
        #      - Stop early if candidates[i] > target (no point exploring further).
        # 3. When target becomes 0 → valid combination → add to result.
        # 4. Move to next index (i + 1) because each number can be used only once.
        #
        # Time Complexity: O(2^n)
        # Space Complexity: O(n) (recursion stack)

        candidates.sort()
        res = []

        def backtrack(start, path, target):
            # If exact target achieved, record combination
            if target == 0:
                res.append(path[:])
                return

            # Explore choices
            for i in range(start, len(candidates)):

                # Skip duplicates (only skip when same level)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If value exceeds target, no need to continue
                if candidates[i] > target:
                    break

                # Recurse with next index (each number used once)
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])

        backtrack(0, [], target)
        return res
