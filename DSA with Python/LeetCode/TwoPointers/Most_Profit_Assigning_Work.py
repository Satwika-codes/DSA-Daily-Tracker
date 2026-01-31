# PROBLEM NUMBER: 826
# https://leetcode.com/problems/most-profit-assigning-work/
# 826. Most Profit Assigning Work
# DIFFICULTY: HARD
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # Approach:
        # - Each job has a difficulty and a profit.
        # - A worker can take any job with difficulty <= their ability.
        # - Sort jobs by difficulty.
        # - Traverse workers in increasing order.
        # - Keep track of the maximum profit seen so far for all doable jobs.
        # - For each worker, assign the best available profit.
        
        # Time Complexity: O(n log n + m log m)
        # Space Complexity: O(n)
        
        
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        total_profit = 0
        best = 0
        j = 0
        
        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                best = max(best, jobs[j][1])
                j += 1
            total_profit += best
        
        return total_profit
