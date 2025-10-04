# PROBLEM NUMBER:2427
# https://leetcode.com/problems/number-of-common-factors/
# DIFFICULTY:Easy
class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        # APPROACH:
        # This solution finds the number of common factors between two integers `a` and `b`.
        # 1. Iterate through numbers from 1 to 1000 (as problem constraints allow).
        # 2. Collect all factors of `a` and `b` separately into `a_fact` and `b_fact`.
        # 3. Compare the two factor lists using nested loops: 
        #    - For each factor of `a`, check if it exists in the factors of `b`.
        #    - Increment `count` for each match.
        # 4. Return `count`, which represents the total number of common factors.
        # This approach explicitly enumerates all factors and counts matches, providing a clear, brute-force solution.
        """
        count=0
        a_fact=[]
        b_fact=[]
        for i in range(1,1001):
            if a%i==0:
                a_fact.append(i)
            if b%i==0:
                b_fact.append(i)
        for j in a_fact:
            for k in b_fact:
                if(j==k):
                    count+=1
            # else:
            #     continue
        return count 
            
