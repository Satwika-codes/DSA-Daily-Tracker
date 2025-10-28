# PROBLEM NUMBER 131
# https://leetcode.com/problems/palindrome-partitioning/
# 131. Palindrome Partitioning
# DIFFICULTY: MEDIUM
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # Approach:
        # 1. Use **backtracking** to explore all possible partitions of the string.
        # 2. At each recursive call:
        #       - Check all possible substrings starting from the current index.
        #       - If a substring is a palindrome, include it in the current path.
        #       - Recursively explore further partitions from the next index.
        # 3. When the starting index reaches the end of the string, 
        #    add the current path (valid palindrome partition) to the result.
        # 4. Use a helper function `is_palindrome()` to check if a substring 
        #    is a palindrome efficiently.
        # 5. Return the list of valid palindrome partitions.
        # Time Complexity: O(2^n), where n is the length of the string.
        # Space Complexity: O(n), where n is the length of the string.
        res = []
        path = []
        
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end)
                    path.pop()
        
        backtrack(0)
        return res
        