# PROBLEM NUMBER: 2149
# https://leetcode.com/problems/rearrange-array-elements-by-sign/
# 2149. Rearrange Array Elements by Sign
# DIFFICULTY: MEDIUM
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach:
        # Step 1: The goal is to rearrange the array so that positive and negative numbers appear alternately while preserving their original relative order.
        # Step 2: First traverse the array and separate the numbers into two lists: one for positive numbers and another for negative numbers.
        # Step 3: Use a simple condition (`num > 0`) to classify numbers and append them to the respective lists.
        # Step 4: Create an empty list `result` to store the final rearranged sequence and initialize two pointers `p` and `n` to track positions in the positive and negative lists.
        # Step 5: Iterate through indices from 0 to the length of the original array.
        # Step 6: For even indices, append the next element from the `positives` list and increment the positive pointer.
        # Step 7: For odd indices, append the next element from the `negatives` list and increment the negative pointer.
        # Step 8: Continue this alternating placement until all elements are used.
        # Step 9: Finally return the `result` list which now contains positives and negatives arranged alternately.
        positives = []
        negatives = []

        # Separate numbers
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        result = []
        p = n = 0

        # Merge alternately
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(positives[p])
                p += 1
            else:
                result.append(negatives[n])
                n += 1

        return result