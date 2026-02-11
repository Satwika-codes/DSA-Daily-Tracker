# PROBLEM NUMBER:825
# https://leetcode.com/problems/friends-of-appropriate-ages/
# 825.Friends Of Appropriate Ages
# DIFFICULTY:MEDIUM
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """

        # Approach:
        # Instead of checking every pair of people (O(n²)),
        # we use counting because age range is limited (1 to 120).

        # Steps:
        # 1. Create a frequency array `count` where:
        #    count[a] = number of people with age 'a'.

        # 2. Iterate over all possible age pairs (ageA, ageB)
        #    from 1 to 120.

        # 3. For each pair, apply the friend request rules:
        #    - ageB must be > 0.5 * ageA + 7
        #    - ageB must be <= ageA
        #    - ageB > 100 and ageA < 100 is invalid

        # 4. If valid:
        #    - If ageA == ageB:
        #        Add count[ageA] * (count[ageA] - 1)
        #        (since a person cannot send request to themselves)
        #    - Otherwise:
        #        Add count[ageA] * count[ageB]

        # Time Complexity:
        # O(n + 120²) ≈ O(n)

        # Space Complexity:
        # O(120) ≈ O(1)
        

        count = [0] * 121
        
        # Count frequency of each age
        for age in ages:
            count[age] += 1
        
        total_requests = 0
        
        # Check all possible age pairs
        for ageA in range(1, 121):
            if count[ageA] == 0:
                continue
                
            for ageB in range(1, 121):
                if count[ageB] == 0:
                    continue
                
                # Apply conditions
                if ageB <= 0.5 * ageA + 7:
                    continue
                if ageB > ageA:
                    continue
                if ageB > 100 and ageA < 100:
                    continue
                
                # If same age, subtract self-request
                if ageA == ageB:
                    total_requests += count[ageA] * (count[ageB] - 1)
                else:
                    total_requests += count[ageA] * count[ageB]
        
        return total_requests
