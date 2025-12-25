# PROBLEM NUMBER:726
# https://leetcode.com/problems/number-of-atoms/
# 726.Number of Atoms
# DIFFICULTY:HARD
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        
        # APPROACH:
        # - Use a stack to handle nested parentheses in the chemical formula.
        # - Maintain a hashmap at each level to count atoms.
        # - When an opening '(' is encountered, push the current map onto the stack.
        # - When a closing ')' is encountered, multiply the atom counts inside the
        #  parentheses by the following number (if any) and merge them back.
        # - Parse element names (capital letter followed by lowercase letters)
        #  and their counts (default is 1 if no number is present).
        # - After processing the entire formula, sort atoms lexicographically
        #   and build the final result string.
    

        from collections import defaultdict

        stack = []
        counts = defaultdict(int)
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(counts)
                counts = defaultdict(int)
                i += 1

            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)

                prev = stack.pop()
                for atom in counts:
                    prev[atom] += counts[atom] * multiplier
                counts = prev

            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]

                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                num = int(formula[start:i] or 1)

                counts[atom] += num

        result = []
        for atom in sorted(counts):
            result.append(atom)
            if counts[atom] > 1:
                result.append(str(counts[atom]))

        return "".join(result)
