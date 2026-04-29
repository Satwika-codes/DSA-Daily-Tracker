# PROBLEM NUMBER:975
# https://leetcode.com/problems/odd-even-jump/
# 975. Odd Even Jump
# DIFFICULTY:HARD
class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Approach:
        # We need count of starting indices from which
        # we can reach the last index using odd/even jump rules.
        #
        # Step 1: Build next jump destinations:
        #
        #         • Odd jump:
        #           next greater or equal value
        #
        #         • Even jump:
        #           next smaller or equal value
        #
        # Step 2: Use sorting + monotonic stack helper
        #         to build next valid jump indices.
        #
        # Step 3: make_next(indices):
        #         • Uses stack to assign next valid jump
        #         • nxt[i] stores where index i jumps next
        #
        # Step 4: Sort indices:
        #         • Increasing values → odd jumps
        #         • Decreasing values → even jumps
        #
        # Step 5: DP arrays:
        #         • odd[i]  = can reach end starting with odd jump
        #         • even[i] = can reach end starting with even jump
        #
        # Step 6: Base case:
        #         • Last index always reaches itself
        #
        # Step 7: Traverse backwards:
        #
        #         If odd jump exists:
        #         • odd[i] = even[next_higher[i]]
        #
        #         If even jump exists:
        #         • even[i] = odd[next_lower[i]]
        #
        # Step 8: Count all indices where odd[i] is True

        n = len(arr)

        def make_next(indices):
            nxt = [-1] * n
            stack = []

            for i in indices:
                while stack and i > stack[-1]:
                    nxt[stack.pop()] = i
                stack.append(i)

            return nxt


        # odd jump: next greater/equal
        sorted_inc = sorted(range(n), key=lambda i: (arr[i], i))
        next_higher = make_next(sorted_inc)

        # even jump: next smaller/equal
        sorted_dec = sorted(range(n), key=lambda i: (-arr[i], i))
        next_lower = make_next(sorted_dec)

        odd = [False] * n
        even = [False] * n

        odd[-1] = even[-1] = True

        for i in range(n-2, -1, -1):

            if next_higher[i] != -1:
                odd[i] = even[next_higher[i]]

            if next_lower[i] != -1:
                even[i] = odd[next_lower[i]]

        return sum(odd)