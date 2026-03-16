# PROBLEM NUMBER: 881
# https://leetcode.com/problems/boats-to-save-people/
# 881. Boats to Save People
# DIFFICULTY: MEDIUM
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # Approach:
        # We need to find the minimum number of boats required to rescue all people.
        # Each boat can carry at most two people and the total weight cannot exceed the limit.
        
        # Step 1: Sort the array of people's weights.
        #         This helps us efficiently pair the lightest and heaviest people.
        
        # Step 2: Use two pointers:
        #         left  → points to the lightest person
        #         right → points to the heaviest person
        
        # Step 3: Initialize a variable "boats" to count the number of boats used.
        
        # Step 4: While left <= right:
        #         • Check if the lightest and heaviest person together fit in one boat.
        #         • If their combined weight ≤ limit:
        #               Move left pointer forward (lightest person paired).
        #         • Always move right pointer backward because the heaviest person
        #           must take a boat in this step.
        
        # Step 5: Increment the boat count for each iteration because
        #         each loop represents one boat being used.
        
        # Step 6: Continue until all people are assigned to boats.
        
        # Step 7: Return the total number of boats required.
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats