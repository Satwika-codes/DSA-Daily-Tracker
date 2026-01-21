class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """       
         # Approach:
         # Use two pointers to scan both strings.

         # Pointer i iterates over s and pointer j iterates over t.
         # Whenever s[i] == t[j], move i forward.
         # Always move j forward.

         # If we can match all characters of s in order while scanning t,
         # then s is a subsequence of t.

         # Time Complexity: O(len(t))
         # Space Complexity: O(1)

        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)
