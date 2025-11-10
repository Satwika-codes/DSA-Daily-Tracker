# PROBLEM NUMBER: 228
# https://leetcode.com/problems/summary-ranges/
# 228. Summary Ranges
# DIFFICULTY: EASY
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Approach:
        # The task is to summarize consecutive ranges in a sorted list of unique integers.
        #     Example: [0,1,2,4,5,7] → ["0->2", "4->5", "7"]
        # We maintain a variable 'start' to mark the beginning of a current range.
        # Traverse the list:
        #     - If the current number is NOT consecutive to the previous one,
        #       it means the previous range ended.
        #     - Add the completed range to the result:
        #         • If start == previous number → single element (e.g., "7")
        #         • Else → range format (e.g., "0->2")
        #     - Update 'start' to the current number.
        # After the loop, add the final pending range
        # Time Complexity: O(n)
        # Space Complexity: O(1) (excluding output list)
        if not nums:
            return []
        res = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(nums[-1]))
        return res