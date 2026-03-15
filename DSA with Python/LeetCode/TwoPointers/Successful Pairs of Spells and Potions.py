class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # Approach:
        # For every spell, we want to know how many potions make:
        # spell * potion >= success
        
        # Step 1: Sort the potions array.
        # Step 2: For each spell, compute the minimum potion value required
        #         so that spell * potion >= success.
        #         potion >= success / spell
        # Step 3: To avoid floating numbers we use ceiling division:
        #         min_potion = (success + spell - 1) // spell
        # Step 4: Use binary search to find the first potion >= min_potion.
        # Step 5: All potions to the right of that index will work.
        # Step 6: Count = total_potions - index
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            # Minimum potion required
            min_potion = (success + spell - 1) // spell

            # Find first potion >= min_potion
            idx = bisect.bisect_left(potions, min_potion)

            result.append(n - idx)

        return result