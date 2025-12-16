# PROBLEM NUMBER: 888
# https://leetcode.com/problems/fair-candy-swap/
# 888.FAIR CANDY SWAP
# DIFFICULTY: EASY
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        # Approach:
        # - Let sumA be the total candies Alice has and sumB be the total candies Bob has.
        # - After swapping one candy each, both should have equal total candies.
        # - Suppose Alice gives candy of size x and Bob gives candy of size y.
        #   Then:
        #       sumA - x + y = sumB - y + x
        # - Rearranging the equation:
        #       y = x + (sumB - sumA) / 2
        # - Compute diff = (sumB - sumA) // 2.
        # - For each candy size x in Alice's list, we check if Bob has a candy
        #   of size y = x + diff.
        # - Use a set for Bob's candies to allow O(1) lookup.
        # - As soon as a valid pair (x, y) is found, return it.
        # Time Complexity: O(n + m)
        # Space Complexity: O(m)
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumB - sumA) // 2
        bobSet = set(bobSizes)
        for x in aliceSizes:
            y = x + diff
            if y in bobSet:
                return [x, y]