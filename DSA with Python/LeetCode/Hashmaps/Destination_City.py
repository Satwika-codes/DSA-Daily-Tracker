# PROBLEM NUMBER:1436
# https://leetcode.com/problems/destination-city/
# 1436.Destination City
# DIFFICULTY:EASY
class Solution(object):
    def destCity(self, paths):
        """
        APPROACH:
        - Each path represents a directed edge from a source city to a destination city.
        - The destination city we want is the one that never appears as a source.
        - Collect all source cities in a set.
        - Traverse destinations and return the city not present in the source set.
        """

        sources = set()

        for src, dest in paths:
            sources.add(src)

        for src, dest in paths:
            if dest not in sources:
                return dest
