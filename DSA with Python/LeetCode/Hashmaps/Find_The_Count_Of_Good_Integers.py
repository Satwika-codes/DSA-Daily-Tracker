# PROBLEM NUMBER: 2426
# https://leetcode.com/problems/find-the-count-of-good-integers/
# Find The Count Of Good Integers
# DIFFICULTY: HARD
class Solution(object):
    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # APPROACH:
        # A number is considered good if its digits can be rearranged to form
        # a k-palindromic integer (a palindrome divisible by k) without leading zeros.

        # Instead of checking all n-digit numbers, we directly generate all
        # k-palindromes of length n and work backwards from them.

        # Steps:
        # 1) Generate palindromes of length n by constructing the first half
        #    and mirroring it.
        # 2) Check if the palindrome is divisible by k.
        # 3) For each valid palindrome, compute its digit frequency.
        # 4) Use a set to ensure each digit frequency (multiset) is processed
        #    only once, avoiding overcounting.
        # 5) For each unique digit frequency, count the number of valid
        #    permutations using combinatorics.
        #    - Total permutations = n! / (product of freq[d]!)
        #    - Subtract permutations that start with zero.
        # 6) Sum the counts across all valid digit frequency patterns.

        # Why this works:
        # - Any good integer must be rearrangeable into at least one valid
        #   k-palindromic number.
        # - Counting by digit frequency guarantees correctness and avoids
        #   duplicate counting.
        # - Generating palindromes instead of all numbers keeps the search space small.

        # Time Complexity:
        # - O(10^(n/2) * n), feasible for n ≤ 10

        # Space Complexity:
        # - O(number of unique digit frequency patterns)
        from math import factorial

        fact = [factorial(i) for i in range(n + 1)]
        seen = set()
        ans = 0

        def count_perms(freq):
            total = fact[n]
            for v in freq:
                total //= fact[v]

            if freq[0] > 0:
                freq[0] -= 1
                bad = fact[n - 1]
                for v in freq:
                    bad //= fact[v]
                freq[0] += 1
                total -= bad

            return total

        half_len = (n + 1) // 2
        start = 10 ** (half_len - 1)
        end = 10 ** half_len

        for half in range(start, end):
            s = str(half)
            pal = s + (s[::-1] if n % 2 == 0 else s[-2::-1])
            num = int(pal)

            if num % k != 0:
                continue

            freq = [0] * 10
            for ch in pal:
                freq[ord(ch) - 48] += 1

            key = tuple(freq)
            if key in seen:
                continue

            seen.add(key)
            ans += count_perms(freq)

        return ans

        