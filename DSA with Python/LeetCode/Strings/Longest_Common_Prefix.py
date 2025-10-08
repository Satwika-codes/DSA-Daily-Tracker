# PROBLEM NUMBER: 14
# https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        # APPROACH:
        # This solution finds the longest common prefix among all strings in the list `strs`.
        # 1. Assume the first string (`strs[0]`) as the initial prefix and store its length in `x`.
        # 2. Iterate through the remaining strings in the list:
        #    - While the current string does not start with the current prefix (`not i.startswith(pref)`):
        #        a) Reduce the prefix length by one (`x -= 1`).
        #        b) If the prefix becomes empty (`x == 0`), return an empty string as there is no common prefix.
        #        c) Update the prefix to the shorter substring (`pref = pref[0:x]`).
        # 3. Once all strings have been checked, return the remaining value of `pref` as the longest common prefix.
        # This approach efficiently trims the prefix until all strings share the same starting substring, achieving O(n * m) complexity, 
        # where n is the number of strings and m is the length of the shortest string.
        """
        pref = strs[0]
        x=len(pref)
        for i in strs[1:]:
            while not i.startswith(pref):
                x-=1
                if x==0:
                    return ""
                pref=pref[0:x]
        return pref
    