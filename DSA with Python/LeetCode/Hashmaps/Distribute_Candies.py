# PROBLEM NUMBER: 575
# https://leetcode.com/problems/distribute-candies/
# Distribute Candies
# DIFFICULTY:EASY
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """

        # find the total number of candies
        # calculate how many candies the sister can eat which is half of total
        # find how many unique types of candies are present
        # sister can eat at most one candy from each unique type
        # the maximum she can eat is the minimum of unique types and allowed candies

        total_candies = len(candyType)
        max_allowed = total_candies // 2
        unique_types = len(set(candyType))
        return min(unique_types, max_allowed)
