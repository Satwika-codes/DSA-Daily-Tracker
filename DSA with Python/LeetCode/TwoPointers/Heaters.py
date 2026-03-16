# PROBLEM NUMBER: 475
# https://leetcode.com/problems/heaters/
# 475. Heaters
# DIFFICULTY: MEDIUM
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # Approach:
        # We need to find the minimum heating radius such that every house
        # is covered by at least one heater.
        
        # Step 1: Sort the heaters array so we can use binary search efficiently.
        
        # Step 2: For each house, find the position where it would be inserted
        #         in the heaters array using binary search (bisect_left).
        
        # Step 3: Compute the distance to the nearest heater:
        #         • Left heater → heaters[pos - 1] if it exists
        #         • Right heater → heaters[pos] if it exists
        
        # Step 4: The effective distance for that house is the minimum of
        #         the left and right heater distances.
        
        # Step 5: Keep track of the maximum distance among all houses,
        #         because the radius must be large enough to cover the
        #         farthest house from its nearest heater.
        
        # Step 6: Return this maximum distance as the required minimum radius.
    
        heaters.sort()
        radius = 0

        for house in houses:
            pos = bisect.bisect_left(heaters, house)

            left_dist = float('inf')
            right_dist = float('inf')

            if pos > 0:
                left_dist = house - heaters[pos - 1]

            if pos < len(heaters):
                right_dist = heaters[pos] - house

            radius = max(radius, min(left_dist, right_dist))

        return radius