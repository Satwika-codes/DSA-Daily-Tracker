# PROBLEM NUMBER: 2337
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/
# 2337.Move Pieces to Obtain a String
# DIFFICULTY: MEDIUM
class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        # Approach:
        # Step 1: The goal is to determine whether the string `start` can be transformed into `target` using valid movements of characters 'L' and 'R' while '_' represents empty spaces.
        # Step 2: First remove all '_' characters from both strings and compare the remaining sequences. If they are not equal, it means the order of 'L' and 'R' differs and transformation is impossible.
        # Step 3: Use two pointers `i` and `j` to traverse the `start` and `target` strings respectively.
        # Step 4: Skip all '_' characters in both strings because they represent empty spaces and do not affect the order of 'L' and 'R'.
        # Step 5: Once both pointers reach actual characters ('L' or 'R'), check the movement rules.
        # Step 6: If the character is 'L', it can only move to the left, so its index in `start` must be greater than or equal to its index in `target`; if `i < j`, it means 'L' moved right, which is invalid.
        # Step 7: If the character is 'R', it can only move to the right, so its index in `start` must be less than or equal to its index in `target`; if `i > j`, it means 'R' moved left, which is invalid.
        # Step 8: If the movement rules are satisfied, move both pointers forward to check the next characters.
        # Step 9: Continue this process until all relevant characters are processed.
        # Step 10: If no rule is violated during traversal, return True indicating the transformation is possible.
        if start.replace('_', '') != target.replace('_', ''):
            return False

        i = j = 0
        n = len(start)

        while i < n and j < n:
            # Skip blanks
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            if i == n or j == n:
                break

            # 2️⃣ Movement rules
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True