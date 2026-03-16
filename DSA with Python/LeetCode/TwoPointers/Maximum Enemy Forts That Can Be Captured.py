# PROBLEM NUMBER: 2511
# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/
# 2511: Maximum Enemy Forts That Can Be Captured
# DIFFICULTY: EASY
class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        # Approach:
        # We need to capture the maximum number of enemy forts between two forts
        # belonging to different players. A valid capture occurs when we have:
        # 1 ... 0 ... 0 ... -1   OR   -1 ... 0 ... 0 ... 1
        # where all forts in between are empty (0).
        
        # Step 1: Initialize a variable "last" to store the index of the last
        #         non-zero fort encountered (either 1 or -1).
        
        # Step 2: Initialize "ans" to store the maximum number of capturable forts.
        
        # Step 3: Traverse the array from left to right.
        
        # Step 4: Whenever we encounter a non-zero fort (1 or -1):
        #         • If we have seen a previous non-zero fort (last != -1)
        #         • AND the current fort is different from the previous one
        #           (forts[i] != forts[last]), then the forts in between are capturable.
        
        # Step 5: The number of forts captured equals:
        #         i - last - 1
        #         Update the maximum value in "ans".
        
        # Step 6: Update "last" to the current index since it is the latest
        #         non-zero fort.
        
        # Step 7: Continue until the array ends.
        
        # Step 8: Return the maximum captured forts.

       
        last = -1
        ans = 0

        for i in range(len(forts)):
            if forts[i] != 0:
                if last != -1 and forts[i] != forts[last]:
                    ans = max(ans, i - last - 1)
                last = i

        return ans