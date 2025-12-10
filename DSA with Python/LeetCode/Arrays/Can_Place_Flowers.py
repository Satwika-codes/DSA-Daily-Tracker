# PROBLEM NUMBER: 605
# https://leetcode.com/problems/can-place-flowers/
# 605. Can Place Flowers
# DIFFICULTY: EASY
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # Approach:
        # We need to check if we can plant `n` flowers in the flowerbed
        # following the rule: No two planted flowers can be adjacent.
        #
        # Idea:
        # - Traverse the array.
        # - At each index `i`, a flower can be planted if:
        #       1. flowerbed[i] == 0   (current spot is empty)
        #       2. left neighbor is empty OR i is the first spot
        #       3. right neighbor is empty OR i is the last spot
        #
        # Steps:
        # 1. Loop through each index.
        # 2. If left & right conditions allow planting:
        #        - Place a flower there (set to 1)
        #        - Increase count
        #        - If count >= n, return True early
        # 3. After loop, return whether count >= n
        #
        # Time Complexity: O(len(flowerbed))
        # Space Complexity: O(1)

        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n
