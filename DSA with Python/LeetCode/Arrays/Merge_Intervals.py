# PROBLEM NUMBER: 56
# https://leetcode.com/problems/merge-intervals/
# 576.  MERGE INTERVALS
# DIFFICULTY: MEDIUM
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Approach:
        # 1.Sort all intervals based on their start time.
        # 2.Initialize an empty list 'merged' to store the result.
        # 3. Iterate through each interval:
        #     - If 'merged' is empty OR current interval does not overlap with the last one, append it.
        #     - Else, merge overlapping intervals by updating the end time to the max end value.
        # 4. Return the merged list.
        # Example:
        # Input: [[1,3],[2,6],[8,10],[15,18]]
        # Output: [[1,6],[8,10],[15,18]]
        # Time Complexity: O(n log n) — due to sorting
        # Space Complexity: O(n) — for storing merged intervals
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged