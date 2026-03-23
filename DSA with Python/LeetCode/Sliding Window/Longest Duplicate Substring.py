# PROBLEM NUMBER: 1044
# https://leetcode.com/problems/longest-duplicate-substring/
# Longest Duplicate Substring
# DIFFICULTY: HARD
class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # We need to find the longest duplicated substring in s.
        #
        # Step 1: Convert characters to numbers (0–25) for hashing.
        #
        # Step 2: Use Binary Search on substring length L:
        #         • left = 1, right = n
        #         • Try to check if a duplicate substring of length L exists.
        #
        # Step 3: For checking a fixed length L, use Rabin-Karp (rolling hash):
        #         • Compute hash of first substring of length L.
        #         • Store it in a set.
        #
        # Step 4: Slide the window:
        #         • Remove left character and add new right character
        #           using rolling hash formula.
        #         • If hash already exists in set → duplicate found.
        #
        # Step 5: If duplicate exists for length L:
        #         • Store starting index
        #         • Try larger length (left = mid + 1)
        #
        # Step 6: If not:
        #         • Try smaller length (right = mid - 1)
        #
        # Step 7: After binary search ends, return substring
        #         starting at recorded index with maximum length.
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]

        mod = 2**63 - 1
        base = 26

        def search(L):
            h = 0
            for i in range(L):
                h = (h * base + nums[i]) % mod

            seen = {h}

            baseL = pow(base, L, mod)

            for i in range(1, n - L + 1):
                h = (h * base - nums[i - 1] * baseL + nums[i + L - 1]) % mod
                if h in seen:
                    return i
                seen.add(h)

            return -1

        left, right = 1, n
        start = -1

        while left <= right:
            mid = (left + right) // 2
            idx = search(mid)

            if idx != -1:
                left = mid + 1
                start = idx
            else:
                right = mid - 1

        return s[start:start + left - 1] if start != -1 else ""
    