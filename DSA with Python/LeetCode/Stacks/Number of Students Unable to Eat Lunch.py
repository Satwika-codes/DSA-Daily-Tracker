# PROBLEM NUMBER:1700
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# 1700. Number of Students Unable to Eat Lunch
# DIFFICULTY: EASY
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        # Approach:
        # Instead of simulating the queue rotations,
        # we only count preferences of students.
        #
        # Step 1: Count students who prefer:
        #         • 0-type sandwiches
        #         • 1-type sandwiches
        #
        # Step 2: Traverse sandwiches stack from top
        #
        # Step 3: For each sandwich:
        #
        #         If sandwich is 0:
        #         • If no student wants 0:
        #             → process stops
        #             → return remaining 1-pref students
        #         • Else use one 0-pref student
        #
        #         If sandwich is 1:
        #         • If no student wants 1:
        #             → process stops
        #             → return remaining 0-pref students
        #         • Else use one 1-pref student
        #
        # Step 4: If all sandwiches served,
        #         return 0

        count0 = students.count(0)
        count1 = students.count(1)

        for s in sandwiches:
            if s == 0:
                if count0 == 0:
                    return count1
                count0 -= 1
            else:
                if count1 == 0:
                    return count0
                count1 -= 1

        return 0