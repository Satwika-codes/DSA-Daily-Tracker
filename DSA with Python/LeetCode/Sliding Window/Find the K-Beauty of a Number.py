# PROBLEM NUMBER:2269
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/
# 2269.Find the K-Beauty of a Number
# DIFFICULTY:EASY
class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        # Approach:
        # We need to count substrings of length k (from the number converted
        # to string) such that the integer value of the substring divides num.
        #
        # Step 1: Convert the integer num into a string to easily extract substrings.
        #
        # Step 2: Iterate over all possible substrings of length k.
        #         (from index 0 to len(s) - k)
        #
        # Step 3: For each substring s[i:i+k]:
        #         • Convert it into an integer "sub".
        #
        # Step 4: Check two conditions:
        #         • sub != 0 (to avoid division by zero)
        #         • num % sub == 0 (sub divides num exactly)
        #
        # Step 5: If both conditions are satisfied, increment the count.
        #
        # Step 6: After checking all substrings, return the count.
        s = str(num)
        count = 0

        for i in range(len(s) - k + 1):
            sub = int(s[i:i+k])

            if sub != 0 and num % sub == 0:
                count += 1

        return count