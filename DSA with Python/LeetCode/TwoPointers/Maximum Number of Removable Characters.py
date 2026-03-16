# PROBLEM NUMBER:1898
# https://leetcode.com/problems/maximum-number-of-removable-characters/
# 1898. Maximum Number of Removable Characters
# DIFFICULTY: HARD
class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        # Approach:
        # We need to find the maximum number of removable characters such that
        # string p is still a subsequence of string s after removals.
        
        # Step 1: Use Binary Search on the number of removable characters (k).
        #         The search range will be from 0 to len(removable).
        
        # Step 2: Create a helper function is_subsequence(k) that checks whether
        #         p is still a subsequence of s after removing the first k indices
        #         from the removable array.
        
        # Step 3: Inside the helper function:
        #         • Put the first k removable indices into a set called "removed".
        #         • Traverse string s while skipping removed indices.
        #         • Use pointer j to track matching characters of p.
        
        # Step 4: If characters match, move pointer j forward.
        #         If j reaches len(p), it means p is a valid subsequence.
        
        # Step 5: Perform Binary Search:
        #         • If p is still a subsequence after removing mid characters,
        #           try removing more characters (move left = mid + 1).
        #         • Otherwise reduce removals (move right = mid - 1).
        
        # Step 6: Keep track of the maximum valid k and return it.

 
        def is_subsequence(k):
            removed = set(removable[:k])
            j = 0

            for i in range(len(s)):
                if i in removed:
                    continue
                if j < len(p) and s[i] == p[j]:
                    j += 1

            return j == len(p)

        left, right = 0, len(removable)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if is_subsequence(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans