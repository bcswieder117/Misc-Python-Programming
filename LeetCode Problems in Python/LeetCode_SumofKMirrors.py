# Blaine Swieder
# LeetCode (Python): Sum of k-Mirror Numbers
# June 22nd, 2025

class Solution(object):
    def kMirror(self, k, n):
        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(x, k):
            res = []
            while x:
                res.append(str(x % k))
                x //= k
            return ''.join(res[::-1]) if res else '0'

        def generate_palindromes():
            # Yield single-digit palindromes first
            for i in range(1, 10):
                yield i
            # Then build multi-digit palindromes
            length = 1
            while True:
                # Even length palindromes
                for half in range(10**(length-1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])
                # Odd length palindromes
                for half in range(10**(length-1), 10**length):
                    s = str(half)
                    for mid in '0123456789':
                        yield int(s + mid + s[::-1])
                length += 1

        gen = generate_palindromes()
        count = 0
        total = 0

        while count < n:
            num = next(gen)
            if is_palindrome(to_base_k(num, k)):
                total += num
                count += 1

        return total

    
    
############ Example Usage #################################

sol = Solution()

print(sol.kMirror(2, 5))  # Expected Output: 25
print(sol.kMirror(3,7))  # Expected Output: 499
