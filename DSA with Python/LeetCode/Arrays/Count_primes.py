# PROBLEM NUMBER: 204
# https://leetcode.com/problems/count-primes/
# 204. Count Primes
# DIFFICULTY: MEDIUM
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Problem:
        # Count how many prime numbers are strictly less than n.

        # Approach:
        # Use the Sieve of Eratosthenes — the fastest method for this task.
        #
        # Key idea:
        # - Create a boolean array is_prime where is_prime[i] tells whether i is prime.
        # - Initially assume all numbers >= 2 are prime.
        # - For each prime p, mark all multiples starting from p*p as non-prime.
        #
        # Optimization:
        # - Loop until p*p < n because any composite < n must have a factor ≤ sqrt(n).
        #
        # Time Complexity: O(n log log n)
        # Space Complexity: O(n)

        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p < n:
            if is_prime[p]:
                # Mark multiples of p starting from p*p
                for i in range(p * p, n, p):
                    is_prime[i] = False
            p += 1

        return sum(is_prime)
