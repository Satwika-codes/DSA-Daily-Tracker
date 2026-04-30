# PROBLEM NUMBER:2589
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/
# 2589. Minimum Time to Complete All Tasks
# DIFFICULTY:HARD

class Solution(object):
    def findMinimumTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        # Approach:
        # We need minimum total time points such that
        # each task gets its required duration within [start, end].
        #
        # Key Idea:
        # Greedy + schedule from rightmost side.
        #
        # Step 1: Sort tasks by end time:
        #         • Earlier deadlines handled first
        #
        # Step 2: Maintain a set "used":
        #         • Stores already occupied time points
        #
        # Step 3: For each task:
        #         • Count how many time points are already used
        #           within its range [start, end]
        #
        # Step 4: Compute remaining needed time:
        #         need = duration - already_used
        #
        # Step 5: If more time needed:
        #         • Fill from right (end → start)
        #         • Choose latest available slots first
        #
        # Step 6: Add selected time points to "used"
        #
        # Step 7: After processing all tasks,
        #         answer = size of used set

        tasks.sort(key=lambda x: x[1])  # sort by end time

        used = set()

        for start, end, duration in tasks:

            # count already used time points
            already = 0
            for t in range(start, end + 1):
                if t in used:
                    already += 1

            need = duration - already

            # fill from right side
            t = end
            while need > 0:
                if t not in used:
                    used.add(t)
                    need -= 1
                t -= 1

        return len(used)