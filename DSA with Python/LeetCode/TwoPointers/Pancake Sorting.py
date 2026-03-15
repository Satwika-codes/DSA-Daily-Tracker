# PROBLEM NUMBER: 969
# https://leetcode.com/problems/pancake-sorting/
# 969. Pancake Sorting
# DIFFICULTY: MEDIUM
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Approach:
        # Pancake Sort works using only "flip" operations.
        # A flip reverses the first k elements of the array.

        # Idea:
        # Step 1: We repeatedly place the largest remaining element in its correct position.
        # Step 2: For each size from n → 2:
        #         • Find the index of the maximum element in arr[0:size]
        #  Step 3: If that element is not already at position size-1:
        #         • First flip it to the front (if needed)
        #         • Then flip the first "size" elements to move it to the end
        # Step 4: Record each flip length in the result list.
        # Step 5: Continue shrinking the working size.
        res = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            # Find index of the maximum element in arr[0:size]
            max_index = arr.index(max(arr[:size]))
            
            # If max element is not already at its correct position
            if max_index != size - 1:
                
                # Step 1: Bring max element to front (if not already there)
                if max_index != 0:
                    res.append(max_index + 1)
                    arr[:max_index + 1] = reversed(arr[:max_index + 1])
                
                # Step 2: Move max element to its correct position
                res.append(size)
                arr[:size] = reversed(arr[:size])
        
        return res