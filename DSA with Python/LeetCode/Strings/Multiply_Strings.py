# PROBLEM NUMBER: 43
# https://leetcode.com/problems/multiply-strings/
# 43.Multiply strings
# DIFFICULTY : MEDIUM
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # APPROACH:
        # This solution multiplies two non-negative integers represented as strings without converting them directly to integers.
        # 1. Handle edge cases: if either `num1` or `num2` is "0", return "0" immediately.
        # 2. Let `m` and `n` be the lengths of `num1` and `num2`. Initialize an array `result` of size `m + n` to store intermediate sums.
        # 3. Iterate over each digit of `num1` and `num2` in reverse (from least significant to most significant):
        #    - Convert characters to integers using `ord(char) - ord('0')`.
        #    - Multiply the current digits and add the product to the appropriate position in `result` (`i + j + 1`).
        #    - Handle carry by updating the previous index (`i + j`).
        # 4. After completing all multiplications, convert the `result` array to a string and strip leading zeros.
        # 5. Return the final product as a string.
        # This approach simulates manual multiplication digit by digit, ensuring correct carry handling and achieving O(m * n) time complexity.
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2   [j]) - ord('0'))
                total = product + result[i + j + 1]
                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        res_str = ''.join(map(str, result)).lstrip('0')
        return res_str if res_str else "0"
        
