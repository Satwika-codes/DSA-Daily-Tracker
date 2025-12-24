# PROBLEM NUMBER : 1399
# https://leetcode.com/problems/count-largest-group/
# 1399.Count Largest Group
# DIFFICULTY:EASY
class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # APPROACH:
        # - For each number from 1 to n, compute the sum of its digits.
        # - Use a hashmap to group numbers by their digit sums.
        # - Find the maximum size among all groups.
        # - Count how many groups have this maximum size and return the count.
        

        groups = {}

        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            groups[digit_sum] = groups.get(digit_sum, 0) + 1

        max_size = max(groups.values())
        return sum(1 for v in groups.values() if v == max_size)
