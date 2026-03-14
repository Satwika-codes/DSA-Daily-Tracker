# PROBLEM NUMBER: 2006
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
# Find All K-Distant Indices in an Array
# DIFFICULTY: MEDIUM
class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        # Approach:
        # Step 1: The goal is to find all indices `j` such that there exists some index `i` where `nums[i] == key` and the distance between them satisfies |i - j| <= k.
        # Step 2: Iterate through the array and whenever an element equal to `key` is found, determine the valid index range around it that satisfies the distance constraint.
        # Step 3: For each such position `i`, compute the starting index of the range as `max(0, i - k)` and the ending index as `min(n - 1, i + k)` so that the range always stays within array bounds.
        # Step 4: Since multiple key occurrences may create overlapping ranges, maintain a variable `last_added` that stores the last index already inserted into the result list to prevent duplicates.
        # Step 5: When adding indices for the current range, start from `max(start, last_added + 1)` so that previously added indices are skipped.
        # Step 6: Append all valid indices from this adjusted start up to `end` into the result list.
        # Step 7: After processing the current key occurrence, update `last_added` to `end` so that future ranges do not re-add the same indices.
        # Step 8: Continue scanning the array for other occurrences of `key` and repeat the same process.
        # Step 9: Finally return the result list containing all indices that are within distance `k` of at least one occurrence of `key`.
        n = len(nums)
        result = []
        last_added = -1  # to avoid duplicates

        for i in range(n):
            if nums[i] == key:
                start = max(0, i - k)
                end = min(n - 1, i + k)

                # Only add new range
                for idx in range(max(start, last_added + 1), end + 1):
                    result.append(idx)

                last_added = end

        return result