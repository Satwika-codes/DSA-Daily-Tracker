# PROBLEM NUMBER: 97
# https://leetcode.com/problems/interleaving-string/
# 97. Interleaving String
# DIFFICULTY: MEDIUM
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # Approach:
        # 1. First, check if the combined lengths of s1 and s2 are equal to s3.
        #    If not, it's impossible for s3 to be formed by interleaving s1 and s2.
        # 2. Use recursion with memoization (top-down DP) to explore all ways
        #    of forming s3 by choosing characters from s1 or s2.
        # 3. Define a helper function helper(i, j, k) where:
        #       i → current index in s1
        #       j → current index in s2
        #       k → current index in s3
        # 4. Base Case:
        #    - If we reach the end of s3, return True only if both s1 and s2
        #      are also fully used (i == len(s1) and j == len(s2)).
        # 5. Recursive Case:
        #    - If s1[i] matches s3[k], recursively try taking from s1.
        #    - If s2[j] matches s3[k], recursively try taking from s2.
        #    - If either leads to a valid interleaving, store True in memo.
        # 6. Use a dictionary (memo) to store already computed (i, j) results
        #    to avoid recomputation (overlapping subproblems).
        # 7. Finally, return the result of helper(0, 0, 0).
        # Time Complexity: O(len(s1) * len(s2))
        # Space Complexity: O(len(s1) * len(s2)) due to recursion + memo
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}
        
        def helper(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if (i, j) in memo:
                return memo[(i, j)]
            
            ans = False
            if i < len(s1) and s1[i] == s3[k]:
                ans = ans or helper(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                ans = ans or helper(i, j + 1, k + 1)
            
            memo[(i, j)] = ans
            return ans
        
        return helper(0, 0, 0)