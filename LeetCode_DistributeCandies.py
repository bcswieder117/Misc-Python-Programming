# Blaine Swieder
# LeetCode (Python): Distribute Candies among Children II
# June 18th, 2025



# I need to go back and learn at a surface level combinatorics after seeing this solution...

class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        
        # Precompute binom(3, i) for i = 0, 1, 2, 3 
        
        C3 = [1, 3, 3, 1]
        
        res = 0
        
        for i in range(4):
            # Subtract i children, each taking (limit + 1) to force the violation.
            T = n - i * (limit + 1) 
            if T < 0:
                break
            # Inclusion - Exclusion Sign
            sign = -1 if (i & 1) else 1
            # The number of non-negative solutions to x1 + x2 + x3 = n' is C(n' + 1, 2)
            ways = (T + 2) * (T + 1) // 2
            res += sign * C3[i] * ways
            
        return res
    

##### Examples #############################################

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1:
    # n = 4 candies, limit = 2 per child
    # Valid distributions of x1+x2+x3=4 with each xi ≤ 2:
    #   (2,2,0), (2,0,2), (0,2,2) → 3 ways
    print(sol.distributeCandies(4, 2))  # Output: 3

    # Example 2:
    # n = 3 candies, limit = 1 per child
    # Only (1,1,1) works → 1 way
    print(sol.distributeCandies(3, 1))  # Output: 1

    # Example 3:
    # n = 5 candies, limit = 3 per child
    # Distributions count = C(5+2,2) - 3*C(1+2,2) + 3*C(-2+2,2) - C(-5+2,2)
    #               = 21 - 9 + 0 - 0 = 12
    print(sol.distributeCandies(5, 3))  # Output: 12
