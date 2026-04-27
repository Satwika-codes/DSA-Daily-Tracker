# PROBLEM NUMBER: 2281
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/
# 2281. Sum of Total Strength of Wizards
# DIFFICULTY: HARD
class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """
        # Approach:
        # We need sum of:
        # (minimum of subarray) * (sum of subarray)
        # over all subarrays.
        #
        # Key Idea:
        # Treat each element as the minimum of some subarrays
        # and compute its total contribution.
        #
        # Step 1: Use monotonic stack to find:
        #         • left[i]  = previous strictly smaller element
        #         • right[i] = next smaller or equal element
        #
        # Step 2: These boundaries tell where strength[i]
        #         acts as minimum.
        #
        # Step 3: Build prefix sums:
        #         • For fast subarray sum calculation
        #
        # Step 4: Build prefix-of-prefix sums:
        #         • Allows fast summation of many subarray sums
        #
        # Step 5: For each index i:
        #         • Compute contribution from left side
        #         • Compute contribution from right side
        #
        # Step 6: Count:
        #         • left_count  = choices on left
        #         • right_count = choices on right
        #
        # Step 7: Compute all subarray sums where strength[i]
        #         is minimum using contribution formula
        #
        # Step 8: Add:
        #         strength[i] * total contribution
        #
        # Step 9: Return answer modulo 1e9+7

        MOD = 10**9 + 7
        n = len(strength)

        # previous strictly smaller
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # next smaller or equal
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = (prefix[i] + strength[i]) % MOD

        # prefix of prefix
        pp = [0] * (n + 2)
        for i in range(n + 1):
            pp[i+1] = (pp[i] + prefix[i]) % MOD

        ans = 0

        for i in range(n):
            l = left[i]
            r = right[i]

            # contributions on right and left
            left_part = (pp[i+1] - pp[max(l,0)+1]) % MOD
            right_part = (pp[r+1] - pp[i+1]) % MOD

            left_count = i - l
            right_count = r - i

            total = (
                right_part * left_count
                - left_part * right_count
            ) % MOD

            ans = (ans + strength[i] * total) % MOD

        return ans % MOD