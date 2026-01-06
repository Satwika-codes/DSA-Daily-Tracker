# PROBLEM NUMBER: 1994
# https://leetcode.com/problems/the-number-of-good-subsets/
# 1994.The Number of Good Subsets
# DIFFICULTY: HARD
class Solution(object):
    def numberOfGoodSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        # Approach:
        # A good subset is one where the product of its elements can be written
        # as a product of distinct primes (no squared prime factor).

        # Steps:
        # 1. Count frequency of each number.
        # 2. Ignore numbers that contain squared prime factors.
        # 3. Represent each valid number by a bitmask of its prime factors.
        # 4. Use DP over bitmasks:
        #    dp[mask] = number of ways to form subsets with used prime factors = mask.
        # 5. For each number, update dp in reverse to avoid reuse.
        # 6. Handle number 1 separately, since it has no prime factors and can be
        #    freely included in any subset.
        # 7. Final answer is sum of all dp[mask] (excluding empty subset),
        #    multiplied by ways to include number 1.

        # This follows the official editorial and avoids overcounting.
        

        MOD = 10**9 + 7
        from collections import Counter

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_index = {p: i for i, p in enumerate(primes)}

        count = Counter(nums)

        def get_mask(x):
            mask = 0
            for p in primes:
                if x % (p * p) == 0:
                    return -1
                if x % p == 0:
                    mask |= 1 << prime_index[p]
            return mask

        dp = [0] * (1 << len(primes))
        dp[0] = 1

        for x in range(2, 31):
            if count[x] == 0:
                continue

            mask = get_mask(x)
            if mask == -1:
                continue

            times = count[x]
            for prev in range((1 << len(primes)) - 1, -1, -1):
                if prev & mask == 0:
                    dp[prev | mask] = (dp[prev | mask] + dp[prev] * times) % MOD

        ones = count[1]
        total = sum(dp) - 1
        total = total * pow(2, ones, MOD) % MOD

        return total
