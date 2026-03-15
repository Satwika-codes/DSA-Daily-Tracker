# PROBLEM NUMBER:763
# https://leetcode.com/problems/partition-labels/
# 763. Partition Labels
# DIFFICULTY: MEDIUM
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # Approach:
        # The goal is to split the string into as many parts as possible such that
        # each letter appears in at most one part.
        
        # Key Idea:
        # A character’s partition must extend until its LAST occurrence in the string.
        # So we first record the last index of every character.
        
        # Step 1: Build a dictionary "last" where
        #         last[ch] = last position of that character in the string.
        #
        # Step 2: Traverse the string and maintain two pointers:
        #         start → beginning of the current partition
        #         end   → farthest last occurrence of characters seen so far
        #
        # Step 3: For each character at index i:
        #         update end = max(end, last[ch])
        #
        # Step 4: If i == end:
        #         it means all characters in the current segment
        #         do not appear later in the string.
        #         So we close the partition.
        #
        # Step 5: Append the partition length (end - start + 1)
        #         and move start to the next position.
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        result = []
        start = 0
        end = 0

        # Step 2: Greedy partitioning
        for i, ch in enumerate(s):
            end = max(end, last[ch])

            # When we reach the end of current partition
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result