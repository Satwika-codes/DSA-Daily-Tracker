# PROBLEM NUMBER: 1475
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# Final Prices With a Special Discount in a Shop
# DIFFICULTY: EASY

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        # Approach:
        # For each price, we need to find the next price to the right
        # that is less than or equal to it (discount).
        #
        # Step 1: Use a monotonic increasing stack:
        #         • Store indices of prices
        #
        # Step 2: Traverse the array:
        #         • For each index i:
        #
        # Step 3: While stack is not empty AND
        #         current price <= price at stack top:
        #         • Pop index from stack
        #         • Apply discount:
        #             prices[idx] -= prices[i]
        #
        # Step 4: Push current index onto stack
        #
        # Step 5: Remaining indices in stack have no discount
        #
        # Step 6: Return modified prices array

        stack = []  # store indices

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                prices[idx] -= prices[i]

            stack.append(i)

        return prices