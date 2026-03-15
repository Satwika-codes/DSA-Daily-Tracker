# PROBLEM NUMBER: 1577
# https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
# 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
# DIFFICULTY: MEDIUM
class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Approach:
        # We need to count triplets where:
        # 1) nums1[i]^2 = nums2[j] * nums2[k]  (j < k)
        # 2) nums2[i]^2 = nums1[j] * nums1[k]
        # Idea:
        # Step 1: Create a helper function count(numsA, numsB).
        # Step 2: Build a frequency map of numsB using Counter.
        # Step 3: For each number x in numsA:
        #         - Compute target = x * x.
        # Step 4: Try all possible factors y in numsB (via the frequency map).
        # Step 5: If y divides target, then z = target // y.
        # Step 6: If z exists in the frequency map:
        #         Case 1: y == z
        #                 → choose any 2 occurrences of y
        #                 → combinations = freq[y] * (freq[y] - 1) // 2
        #         Case 2: y < z
        #                 → multiply their frequencies freq[y] * freq[z]
        #                 (y < z avoids double counting).
        # Step 7: Sum all valid combinations.
        # Step 8: Compute both directions:
        #         nums1² vs nums2 products
        #         nums2² vs nums1 products.
        def count(numsA, numsB):
            freq = Counter(numsB)
            total = 0

            for x in numsA:
                target = x * x

                for y in freq:
                    if target % y == 0:
                        z = target // y
                        if z in freq:
                            if y == z:
                                total += freq[y] * (freq[y] - 1) // 2
                            elif y < z:
                                total += freq[y] * freq[z]

            return total

        return count(nums1, nums2) + count(nums2, nums1)