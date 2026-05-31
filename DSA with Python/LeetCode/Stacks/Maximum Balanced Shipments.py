# PROBLEM NUMBER: 3638
# https://leetcode.com/problems/maximum-balanced-shipments/
# 3638.Maximum Balanced Shipments
# DIFFICULTY: MEDIUM

class Solution(object):
    def maxBalancedShipments(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """

        # Approach:
        # We greedily form the maximum number
        # of balanced shipments.
        #
        # A shipment is considered balanced when
        # its last package has a weight smaller
        # than the maximum weight seen within
        # that shipment.
        #
        # Step 1:
        # Start building a shipment from
        # the current position.
        #
        # Step 2:
        # Track:
        #
        # • start of shipment
        # • current maximum weight
        #
        # Step 3:
        # Expand the shipment by moving forward.
        #
        # • Update the maximum weight seen so far.
        #
        # Step 4:
        # If the current package weight is
        # smaller than the shipment maximum:
        #
        # • A valid balanced shipment is formed.
        #
        # • Increase answer.
        #
        # • Start building the next shipment.
        #
        # Step 5:
        # Continue until all packages
        # have been processed.
        #
        # Step 6:
        # Return the maximum number
        # of balanced shipments formed.

        n = len(weight)

        ans = 0

        i = 0

        while i < n:

            # Start a new shipment
            start = i

            current_max = weight[i]

            i += 1

            # Expand shipment
            while i < n:

                current_max = max(
                    current_max,
                    weight[i]
                )

                # Balanced shipment found
                if weight[i] < current_max:

                    ans += 1

                    i += 1

                    break

                i += 1

        return ans