# PROBLEM NUMBER: 388
# https://leetcode.com/problems/longest-absolute-file-path/
# 388. Longest Absolute File Path
# DIFFICULTY: MEDIUM

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        # Approach:
        # The file system is represented as a string
        # where:
        #
        # • '\n' separates files/directories
        # • '\t' represents depth level
        #
        # We keep track of the total path length
        # at each depth using a hashmap.
        #
        # Step 1:
        # Initialize:
        #
        # • max_len = 0
        #   Stores longest absolute file path.
        #
        # • path_len = {0: 0}
        #   Stores cumulative path length
        #   for every depth.
        #
        # Step 2:
        # Split input by '\n'
        # so each line represents
        # a file or directory.
        #
        # Step 3:
        # For each line:
        #
        # • Remove leading tabs
        #   to get actual name.
        #
        # • Depth =
        #   Number of leading tabs.
        #
        # Step 4:
        # If name contains '.':
        # • It is a file.
        #
        # • Complete path length =
        #   path length till parent directory
        #   + file name length.
        #
        # • Update maximum answer.
        #
        # Step 5:
        # Otherwise it is a directory.
        #
        # • Store path length for
        #   next depth level.
        #
        # • Add:
        #   directory name length
        #   + 1 for '/' separator.
        #
        # Step 6:
        # Return maximum file path length found.

        max_len = 0

        # depth -> cumulative path length
        path_len = {0: 0}

        for line in input.split('\n'):

            # Remove leading tabs
            name = line.lstrip('\t')

            # Calculate depth
            depth = len(line) - len(name)

            # File
            if '.' in name:

                max_len = max(
                    max_len,
                    path_len[depth] + len(name)
                )

            # Directory
            else:

                path_len[depth + 1] = (
                    path_len[depth] +
                    len(name) +
                    1  # '/' separator
                )

        return max_len