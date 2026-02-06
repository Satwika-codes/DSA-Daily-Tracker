# PROBLEM NUMBER: 786
# https://leetcode.com/problems/k-th-smallest-prime-fraction/
# 786.K-th Smallest Prime Fraction
# DIFFICULTY: HARD
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """   
        # Approach:
        # ---------
        # We use Binary Search on the value of fractions instead of generating
        # all possible fractions.

        # 1. The smallest possible fraction is 0 and the largest is 1.
        # 2. Perform binary search between low = 0.0 and high = 1.0.
        # 3. For a chosen mid value:
        #    - Count how many fractions arr[i] / arr[j] are <= mid.
        #    - While counting, also track the maximum fraction that is <= mid.
        # 4. If count == k:
        #    - The tracked maximum fraction is the k-th smallest fraction.
        # 5. If count < k:
        #    - Move the search range to the right (low = mid).
        # 6. If count > k:
        #    - Move the search range to the left (high = mid).
        # 7. Repeat until the k-th smallest fraction is found.

        # This avoids generating all fractions and works efficiently
        # in O(n log n) time.
        

        n = len(arr)
        low, high = 0.0, 1.0

        while True:
            mid = (low + high) / 2
            count = 0
            max_num = 0
            max_den = 1
            j = 1

            for i in range(n):
                while j < n and arr[i] > mid * arr[j]:
                    j += 1
                if j == n:
                    break

                count += n - j

                if arr[i] * max_den > max_num * arr[j]:
                    max_num = arr[i]
                    max_den = arr[j]

            if count == k:
                return [max_num, max_den]
            elif count < k:
                low = mid
            else:
                high = mid
