# PROBLEM NUMBER :833
# https://leetcode.com/problems/find-and-replace-in-string/
# 833.Find and Replace string
# DIFFICULTY:MEDIUM
class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        APPROACH:
        1. Combine indices, sources, and targets into a single list of tuples.
        2. Sort the replacements by index so replacements are processed from
           left to right.
        3. Iterate through the string using a pointer and apply a replacement
           only when the source string matches the substring starting at
           the given index.
        4. If no replacement applies at the current position, append the
           original character.
        5. Continue until the entire string is processed and return the result.

        Time Complexity:
        - O(n + total length of sources)

        Space Complexity:
        - O(n)
        """
        replacements = sorted(zip(indices, sources, targets))
        res = []
        i = 0

        for idx, src, tgt in replacements:
            if i < idx:
                res.append(s[i:idx])
                i = idx
            if s[idx:idx + len(src)] == src:
                res.append(tgt)
                i += len(src)

        res.append(s[i:])
        return "".join(res)
