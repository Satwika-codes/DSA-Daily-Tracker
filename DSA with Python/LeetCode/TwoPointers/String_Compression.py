# PROBLEM NUMBER: 443
# https://leetcode.com/problems/string-compression/
# 443. String Compression
# DIFFICULTY: MEDIUM
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # APPROACH:
        # ---------
        # We use two pointers to compress the array in-place.

        # Read Pointer (i):
        #    - Traverses the input array to count consecutive repeating characters.

        # Write Pointer (write):
        #    - Writes the compressed result back into the same array.

        # Steps:
        # - Start from index i = 0.
        # - For each group of identical characters:
        #     • Count how many times it appears consecutively.
        #     • Write the character at the write position.
        #     • If count > 1, write each digit of the count separately.
        # - Move i to the next new character.
        # - Return the final write pointer as the new length.

        # Important:
        # - The compression must be done in-place.
        # - Extra characters beyond the returned length are ignored.

        # Time Complexity: O(n)
        # Space Complexity: O(1)


        write = 0
        i = 0
        n = len(chars)

        while i < n:
            ch = chars[i]
            count = 0

            # count occurrences
            while i < n and chars[i] == ch:
                i += 1
                count += 1

            # write character
            chars[write] = ch
            write += 1

            # write count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
