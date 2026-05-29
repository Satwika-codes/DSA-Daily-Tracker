# PROBLEM NUMBER: 1096
# https://leetcode.com/problems/brace-expansion-ii/
# 1096. Brace Expansion II
# DIFFICULTY: HARD

class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """

        # Approach:
        # We recursively parse the expression
        # using DFS + Set Operations.
        #
        # Operations involved:
        #
        # • Union:
        #   {a,b} → combine results
        #
        # • Concatenation:
        #   {a,b}{c,d} → ac, ad, bc, bd
        #
        # We use recursion to process nested braces.
        #
        # Step 1:
        # Create helper function 'product'
        # to generate concatenation combinations.
        #
        # Example:
        # set1 = {"a", "b"}
        # set2 = {"c", "d"}
        #
        # Result:
        # {"ac", "ad", "bc", "bd"}
        #
        # Step 2:
        # Create recursive parser function parse(i)
        # where i is current index.
        #
        # Variables:
        #
        # • res:
        #   Stores union results
        #
        # • cur:
        #   Stores current concatenation results
        #
        # Step 3:
        # Process characters one by one.
        #
        # Case 1: Alphabet
        # • Concatenate current character
        #
        # Case 2: '{'
        # • Recursively parse sub-expression
        # • Concatenate returned set
        #
        # Case 3: ','
        # • Current expression ends
        # • Add current results into res
        # • Reset current set
        #
        # Case 4: '}'
        # • End current recursion level
        # • Return accumulated result
        #
        # Step 4:
        # Parse entire expression from index 0.
        #
        # Step 5:
        # Return sorted final result.

        # Generates concatenation combinations
        def product(set1, set2):
            return {a + b for a in set1 for b in set2}

        # Recursive parser
        def parse(i):

            # Stores union results
            res = set()

            # Stores current concatenation
            cur = {""}

            while i < len(expression):

                # Alphabet character
                if expression[i].isalpha():

                    # Concatenate character
                    cur = product(cur, {expression[i]})
                    i += 1

                # Nested brace expression
                elif expression[i] == '{':

                    # Parse sub-expression
                    sub, i = parse(i + 1)

                    # Concatenate with current
                    cur = product(cur, sub)

                # Union separator
                elif expression[i] == ',':

                    # Add current results
                    res |= cur

                    # Reset current set
                    cur = {""}

                    i += 1

                # End of current brace
                elif expression[i] == '}':

                    # Add remaining current results
                    res |= cur

                    return res, i + 1

            # Add remaining results
            res |= cur

            return res, i

        # Parse complete expression
        ans, _ = parse(0)

        # Return sorted output
        return sorted(ans)