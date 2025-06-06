# Blaine Swieder
# June 5th, 2025
# LeetCode Problem: Using a Robot to Print the Lexicographically Smallest String




from collections import Counter

class Solution:
    def robotWithString(self, s):
        """
        This function simulates a robot writing the lexicographically smallest string
        by using a stack and two operations: push and pop.
        
        Parameters:
        s (str): The input string

        Returns:
        str: The lexicographically smallest string achievable
        """
        count = Counter(s)       # Track how many of each character remain
        t = []                   # Stack the robot uses
        result = []             # Final output string (as list for speed)
        min_char = 'a'           # Start looking for smallest characters

        for char in s:
            t.append(char)       # Push operation
            count[char] -= 1     # One less of this character now

            # Move min_char forward until it points to a character still in 's'
            while min_char <= 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # Pop from the stack if it is safe to write the top of the stack
            while t and t[-1] <= min_char:
                result.append(t.pop())

        # Pop any remaining characters
        while t:
            result.append(t.pop())

        return ''.join(result)

sol = Solution()

print(sol.robotWithString("zza"))      # Output: "azz"
print(sol.robotWithString("sqbd"))     # Output: "bdqs"
print(sol.robotWithString("zxby"))     # Output: "bxyz"
print(sol.robotWithString("bcd"))      # Output: "bcd"

