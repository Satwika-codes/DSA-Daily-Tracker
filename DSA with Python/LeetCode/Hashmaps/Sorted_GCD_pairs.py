class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """

        """
        Approach:
        We consider all unordered pairs (i < j) and compute gcd(nums[i], nums[j]).
        Instead of computing gcd for every pair, we use number theory.

        Steps:
        1. Count frequency of each value.
        2. For each possible gcd g from max(nums) down to 1:
           - Count how many numbers are divisible by g.
           - Total pairs with gcd multiple of g = C(cnt, 2).
        3. Use inclusion-exclusion to compute the number of pairs
           with gcd exactly equal to g.
        4. Build a prefix sum array where prefix[g] = number of pairs
           with gcd <= g.
        5. For each query q, binary search the smallest g such that
           prefix[g] > q.

        This avoids pairwise gcd computation and runs efficiently.
        """

        from collections import Counter
        import bisect

        max_val = max(nums)
        freq = Counter(nums)

        cnt = [0] * (max_val + 1)
        for x in freq:
            cnt[x] = freq[x]

        gcd_pairs = [0] * (max_val + 1)

        for g in range(max_val, 0, -1):
            total = 0
            for multiple in range(g, max_val + 1, g):
                total += cnt[multiple]
            gcd_pairs[g] = total * (total - 1) // 2
            for multiple in range(2 * g, max_val + 1, g):
                gcd_pairs[g] -= gcd_pairs[multiple]

        prefix = []
        running = 0
        for g in range(1, max_val + 1):
            running += gcd_pairs[g]
            prefix.append(running)

        ans = []
        for q in queries:
            ans.append(bisect.bisect_right(prefix, q) + 1)

        return ans
