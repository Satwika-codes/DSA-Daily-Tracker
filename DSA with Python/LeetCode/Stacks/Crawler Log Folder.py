# PROBLEM NUMBER: 1598
# https://leetcode.com/problems/crawler-log-folder/
# 1598. Crawler Log Folder
# DIFFICULTY: EASY

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """

        # Approach:
        # We simulate folder navigation operations.
        #
        # Operations:
        #
        # • "../"
        #   → Move to parent folder
        #
        # • "./"
        #   → Stay in current folder
        #
        # • "x/"
        #   → Move into child folder
        #
        # Step 1:
        # Maintain a variable 'depth'
        # representing current folder depth.
        #
        # Step 2:
        # Traverse each operation in logs.
        #
        # Step 3:
        # If operation is "../":
        # • Move one level up
        # • But depth cannot go below 0
        #
        # Step 4:
        # If operation is "./":
        # • Do nothing
        #
        # Step 5:
        # Otherwise:
        # • Move into a child folder
        # • Increase depth
        #
        # Step 6:
        # Final depth represents
        # minimum operations needed
        # to return to main folder.

        depth = 0

        for log in logs:

            # Move to parent folder
            if log == "../":
                if depth > 0:
                    depth -= 1

            # Stay in same folder
            elif log == "./":
                continue

            # Move into child folder
            else:
                depth += 1

        return depth