# PROBLEM NUMBER: 632
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# 632. Smallest Range Covering Elements from K Lists
# DIFFICULTY: HARD
import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Approach:
        # We need to find the smallest range [L, R] such that
        # at least one element from each list is included in this range.
        #
        # Step 1: Use a min-heap to track the smallest element among
        #         the current elements of all lists.
        #
        # Step 2: Insert the first element of each list into the heap.
        #         Also track the current maximum among these elements.
        #
        # Step 3: Initialize best_range to a very large range.
        #
        # Step 4: Repeat:
        #         • Pop the minimum element from the heap.
        #         • This gives current_min.
        #
        # Step 5: Compare current range [current_min, current_max]
        #         with best_range and update if smaller.
        #
        # Step 6: Move to the next element in the same list from which
        #         current_min was taken.
        #
        # Step 7: If that list is exhausted, break because we can no longer
        #         include at least one element from each list.
        #
        # Step 8: Push the next element into the heap and update current_max.
        #
        # Step 9: Continue until one list runs out, then return best_range.

        k = len(nums)
        heap = []
        current_max = float('-inf')
        
        # Step 1: Put first element of each list in heap
        for i in range(k):
            val = nums[i][0]
            heapq.heappush(heap, (val, i, 0))  # (value, list_index, element_index)
            current_max = max(current_max, val)
        
        best_range = [float('-inf'), float('inf')]
        
        # Step 2: Process heap
        while True:
            current_min, list_idx, elem_idx = heapq.heappop(heap)
            
            # Update best range
            if (current_max - current_min < best_range[1] - best_range[0] or
                (current_max - current_min == best_range[1] - best_range[0] and
                 current_min < best_range[0])):
                best_range = [current_min, current_max]
            
            # Move to next element in same list
            if elem_idx + 1 == len(nums[list_idx]):
                break  # One list exhausted → cannot cover all lists anymore
            
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            
            # Update current max
            current_max = max(current_max, next_val)
        
        return best_range
        