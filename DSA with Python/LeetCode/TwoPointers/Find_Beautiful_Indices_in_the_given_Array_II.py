# PROBLEM NUMBER: 3008
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array/
# 3008.Find Beautiful Indices in the given Array II
# DIFFICULTY: HARD
class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        # Approach:
        # 1. Use KMP to find all occurrences of string `a` in `s`.
        # 2. Use KMP to find all occurrences of string `b` in `s`.
        # 3. Use two pointers to check if any index of `b` lies within
        #    distance `k` for each index of `a`.

        # Time Complexity: O(n)
        # Space Complexity: O(n)

        def kmp_search(text, pattern):
            n, m = len(text), len(pattern)
            lps = [0] * m

            # Build LPS array
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j

            res = []
            j = 0
            for i in range(n):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    res.append(i - m + 1)
                    j = lps[j - 1]

            return res

        A = kmp_search(s, a)
        B = kmp_search(s, b)

        res = []
        j = 0

        for i in A:
            while j < len(B) and B[j] < i - k:
                j += 1
            if j < len(B) and abs(B[j] - i) <= k:
                res.append(i)

        return res
