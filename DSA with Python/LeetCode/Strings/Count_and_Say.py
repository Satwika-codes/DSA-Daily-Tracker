# PROBLEM NUMBER: 38
# https://leetcode.com/problems/count-and-say/
# Count and Say
# Difficulty: MEDIUM
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # APPROACH:
        # This solution generates the nth term in the "Count and Say" sequence using iterative construction.
        # 1. Base case: if n == 1, return "1" (the first term of the sequence).
        # 2. Initialize `prev` as "1" (the first sequence term).
        # 3. For each term from 2 to n:
        #    - Initialize an empty string `res` to build the next sequence term.
        #    - Initialize a counter `count = 1`.
        #    - Traverse the previous term (`prev`) starting from index 1:
        #        a) If the current character equals the previous one, increment `count`.
        #        b) If it differs, append the count and the previous character to `res`, then reset `count` to 1.
        #    - After the loop, append the count and the last character of `prev` to `res`.
        #    - Update `prev` to `res` for the next iteration.
        # 4. Return the final `prev` after processing all n terms.
        # This approach uses run-length encoding logic to describe the previous sequence term, achieving O(n * m) time complexity, 
        # where m is the length of the sequence term.
        if n==1:
            return "1"
        prev="1"
        for i in range(2,n+1):
            res=""
            count=1
            for j in range(1, len(prev)):
                if prev[j]==prev[j-1]:
                    count+=1
                else:
                    res+=str(count)+prev[j-1]
                    count=1
            res += str(count) + prev[-1]
            prev = res
        return prev