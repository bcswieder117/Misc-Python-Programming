# Blaine Swieder
# LeetCode (Python3): Maximum Matching of Players with Trainers
# July 13th, 2025

from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sort both lists
        players.sort()
        trainers.sort()
        
        i = j = matches = 0
        n, m = len(players), len(trainers)
        
        # Greedily match weakest player with weakest sufficient trainer
        while i < n and j < m:
            if players[i] <= trainers[j]:
                matches += 1
                i += 1
                j += 1
            else:
                # Trainer too weak, try next trainer
                j += 1
        
        return matches


##### Example Usage Cases #######################################################

# Instantiate solver
sol = Solution()

# Define test cases
tests = [
    # Example cases
    ([4, 7, 9], [8, 2, 5, 8], 2),
    ([1, 1, 1], [10], 1),
    # Edge cases
    ([1], [1], 1),
    ([5, 6], [1, 2, 3], 0),
    ([1, 2, 3], [1, 2, 3], 3),
    ([9, 4, 7], [8, 2, 5, 8], 2),
    ([2, 2, 2, 2], [2, 2], 2),
]

# Run and report
for idx, (players, trainers, expected) in enumerate(tests, start=1):
    result = sol.matchPlayersAndTrainers(players, trainers)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test {idx}: players = {players}, trainers = {trainers}, expected = {expected}, got = {result} -> {status}")
