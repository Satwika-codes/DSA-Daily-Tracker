# PROBLEM NUMBER: 986
# https://leetcode.com/problems/interval-list-intersections/
# 986. Interval List Intersections
# DIFFICULTY: MEDIUM
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        # Approach:
        # We are given two lists of intervals (firstList and secondList) that are already
        # sorted and non-overlapping within themselves. Our goal is to find the intersection
        # intervals between the two lists.
        
        # Step 1: Use two pointers:
        #         i → pointer for firstList
        #         j → pointer for secondList
        
        # Step 2: Traverse both lists while i < len(firstList) and j < len(secondList).
        
        # Step 3: For the current intervals:
        #         firstList[i] = [start1, end1]
        #         secondList[j] = [start2, end2]
        
        # Step 4: Compute the possible intersection:
        #         start = max(start1, start2)
        #         end   = min(end1, end2)
        
        # Step 5: If start <= end, it means the intervals overlap.
        #         Add [start, end] to the result list.
        
        # Step 6: Move the pointer of the interval that finishes earlier.
        #         • If end1 < end2 → increment i
        #         • Otherwise → increment j
        #         This ensures we don't miss any future intersections.
        
        # Step 7: Continue until one of the lists is completely traversed.
        
        # Step 8: Return the list of intersection intervals.

     
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                result.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result