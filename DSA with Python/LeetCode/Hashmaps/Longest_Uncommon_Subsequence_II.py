# PROBLEM NUMBER:522
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/
# Longest Uncommon Subsequence II
# DIFFICULTY: Hard
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # APPROACH:
        # 1. Sort all strings in descending order of length so we try longer
        #    candidates first.
        # 2. For each string, check whether it is a subsequence of any other
        #    string in the list.
        # 3. A string is considered an uncommon subsequence if it is NOT a
        #    subsequence of any other string.
        # 4. The first string (longest) that satisfies this condition is the
        #    answer.
        # 5. If no such string exists, return -1.

        # Time Complexity:
        # - O(n^2 * L), where L is the maximum string length

        # Space Complexity:
        # - O(1)
        
        strs.sort(key=len, reverse=True)

        def is_subseq(a, b):
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)

        for i in range(len(strs)):
            uncommon = True
            for j in range(len(strs)):
                if i != j and is_subseq(strs[i], strs[j]):
                    uncommon = False
                    break
            if uncommon:
                return len(strs[i])

        return -1
