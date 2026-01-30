# PROBLEM NUMBER: 165
# https://leetcode.com/problems/compare-version-numbers/
# 165.Compare Version Numbers
# DIFFICULTY: MEDIUM
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Approach:
        # - Split both version strings by '.' to get revision numbers.
        # - Convert each revision into an integer to ignore leading zeros.
        # - Compare corresponding revisions one by one.
        # - If one version has fewer revisions, treat missing revisions as 0.
        # - Return:
        #   1  if version1 > version2
        #  -1  if version1 < version2
        #   0  if both versions are equal.
        # - Time Complexity: O(max(n, m))
        # - Space Complexity: O(n + m)
        
        
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        n = max(len(v1), len(v2))
        
        for i in range(n):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            
            if num1 > num2:
                return 1
            if num1 < num2:
                return -1
        
        return 0
