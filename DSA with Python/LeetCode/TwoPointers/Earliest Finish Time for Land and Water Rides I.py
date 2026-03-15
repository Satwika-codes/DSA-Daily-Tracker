# PROBLEM NUMBER: 3633
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
# 3633. Earliest Finish Time for Land and Water Rides I
# DIFFICULTY: EASY
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        # Approach:
        # We must perform one land ride and one water ride.
        # They can be done in either order:
        #   1) Land → Water
        #   2) Water → Land
        #
        # For each pair of rides we compute the earliest possible finish time.
        
        # Land → Water
        # Step 1: Finish the land ride
        #         finish_land = landStartTime[i] + landDuration[i]
        # Step 2: Water ride can only start after both:
        #         • the land ride finishes
        #         • its own start time
        #         start_water = max(finish_land, waterStartTime[j])
        # Step 3: Compute finish time
        #         finish_time = start_water + waterDuration[j]
        
        # Water → Land
        # Step 4: Same logic but reversed order.
        
        # Step 5: Track the minimum finish time across all possibilities.

        min_time = float('inf')

        # Land -> Water
        for i in range(len(landStartTime)):
            finish_land = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                start_water = max(finish_land, waterStartTime[j])
                finish_time = start_water + waterDuration[j]
                min_time = min(min_time, finish_time)

        # Water -> Land
        for j in range(len(waterStartTime)):
            finish_water = waterStartTime[j] + waterDuration[j]

            for i in range(len(landStartTime)):
                start_land = max(finish_water, landStartTime[i])
                finish_time = start_land + landDuration[i]
                min_time = min(min_time, finish_time)

        return min_time