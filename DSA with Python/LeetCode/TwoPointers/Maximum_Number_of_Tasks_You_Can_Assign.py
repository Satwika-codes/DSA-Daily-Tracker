# PROBLEM NUMBER: 2071
# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign
# 2071. Maximum Number of Tasks You Can Assign
# DIFFICULTY: HARD
class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        # Approach:
        # - Sort tasks and workers.
        # - Binary search on the number of tasks that can be assigned.
        # - For a given mid:
        #     • Take the mid smallest tasks.
        #     • Take the mid strongest workers.
        #     • Assign tasks from hardest to easiest.
        #     • If a worker cannot do a task normally, use a pill if possible.
        

        import bisect

        tasks.sort()
        workers.sort()

        def can(mid):
            w = workers[-mid:]          # strongest `mid` workers
            t = tasks[:mid]             # easiest `mid` tasks
            p = pills

            i = mid - 1                 # task pointer (hardest)
            j = mid - 1                 # worker pointer (strongest)

            while i >= 0:
                if w[j] >= t[i]:
                    j -= 1
                    i -= 1
                else:
                    if p == 0:
                        return False
                    # use pill on weakest worker that can do task
                    idx = bisect.bisect_left(w, t[i] - strength)
                    if idx > j:
                        return False
                    p -= 1
                    w.pop(idx)
                    j -= 1
                    i -= 1

            return True

        left, right = 0, min(len(tasks), len(workers))
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
