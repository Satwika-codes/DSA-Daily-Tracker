# PROBLEM NUMBER: 860
# https://leetcode.com/problems/lemonade-change/
# 860. Lemonade Change
# DIFFICULTY: EASY
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        # Approach:
        # Step 1: We simulate a lemonade stand where each lemonade costs $5.
        #         Customers may pay with $5, $10, or $20 bills.
        #
        # Step 2: Maintain two counters:
        #         • five → number of $5 bills
        #         • ten  → number of $10 bills
        #
        # Step 3: For each bill:
        #         • If bill = 5 → simply take it.
        #
        #         • If bill = 10:
        #             - Must give back one $5.
        #             - If no $5 available → return False.
        #
        #         • If bill = 20:
        #             - Prefer giving change using one $10 + one $5 
        #               (optimal, saves $5 bills).
        #             - If that’s not possible, try giving three $5 bills.
        #             - If neither possible → return False.
        #
        # Step 4: If we finish processing all bills successfully,
        #         return True.

        five = ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
