# PROBLEM NUMBER: 57
# https://leetcode.com/problems/insert-interval/
# 57. Insert Interval
# DIFFICULTY: MEDIUM
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # Approach:
        # Add all intervals that end before the new interval starts (no overlap).
        # Merge all overlapping intervals with the new interval by expanding its start and end.
        # Add the merged interval.
        # Add all intervals that come after the merged one.
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        res = []
        i = 0
        n = len(intervals)
        start, end = newInterval

        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        while i < n:
            res.append(intervals[i])
            i += 1

        return res