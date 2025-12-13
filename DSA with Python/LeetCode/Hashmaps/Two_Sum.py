# PROBLEM NUMBER :1
# https://leetcode.com/problems/two-sum
# 1.Two Sum
# DIFFICULTY:EASY
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #  APPROACH 
        # Step 1: Use a hash map (dictionary) to store numbers we have seen so far
        #         along with their indices.
        #
        # Step 2: Traverse the array using index and value.
        #
        # Step 3: For each number, calculate the required complement:
        #         complement = target - current number.
        #
        # Step 4: Check if the complement already exists in the hash map.
        #         - If yes, we have found the two indices whose values add up to target.
        #         - Return the stored index of the complement and the current index.
        #
        # Step 5: If not found, store the current number with its index in the map.
        #
        # Step 6: Since exactly one solution exists, the answer will be returned
        #         during the traversal.

        seen = {}
        
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
