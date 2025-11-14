# PROBLEM NUMBER: 135
# https://leetcode.com/problems/candy/
# 135.Candy
# DIFFICULTY: HARD
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # APPROACH (Two-pass Greedy):
        # Goal: Every child gets at least 1 candy.
        # Children with higher rating than neighbors must get more candies.
        # Strategy:
        # 1.Create an array 'candies' initialized with 1 for all children.
        #     Because each child must receive at least one candy.
        # 2.LEFT → RIGHT PASS
        #     If ratings[i] > ratings[i-1], then candies[i] = candies[i-1] + 1
        #     This ensures increasing sequence from the left side.
        # 3.RIGHT → LEFT PASS
        #     If ratings[i] > ratings[i+1], then candies[i] must be
        #     max(candies[i], candies[i+1] + 1)
        #     This ensures correctness from the right side while keeping the higher requirement.
        # 4.Final answer = sum(candies)
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(ratings)
        candies = [1] * n       
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)