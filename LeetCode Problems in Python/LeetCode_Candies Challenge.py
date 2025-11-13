# Blaine Swieder
# June 2nd, 2025
# LeetCode Challenge: Candy


# This problem — Leetcode 135: Candy — is a classic greedy algorithm problem. The goal is to assign the minimum number of candies such that:
# 1) Every child gets at least one candy.
# 2) Children with a higher rating than their neighbors get more candies.

#  Strategy (Two Pass Greedy): 
#  First, initialize all candies to 1 (minimum requirement).
#  Then:
#  1) Left to right pass: if ratings[i] > ratings[i - 1], increase candies[i] = candies[i - 1] + 1.
#  2) Right to left pass: if ratings[i] > ratings[i + 1], set candies[i] = max(candies[i], candies[i + 1] + 1).


from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Step 1: everyone gets at least 1

        # Step 2: Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


if __name__ == "__main__":
    solution = Solution()

    print(solution.candy([1, 0, 2]))  # Output: 5
    print(solution.candy([1, 2, 2]))  # Output: 4
    print(solution.candy([1, 3, 4, 5, 2]))  # Output: 11
