# Blaine Swieder
# LeetCode (Python3): Finding Pairs with a Certain Sum
# July 6th, 2025

from typing import List
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val

        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0:
            del self.counter2[old_val]
        self.counter2[new_val] += 1

        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        result = 0
        for num in self.nums1:
            complement = tot - num
            result += self.counter2.get(complement, 0)
        return result

##### Example Usage ######################################

nums1 = [1, 1, 2, 2, 2]
nums2 = [1, 2, 3, 4, 5]
fsp = FindSumPairs(nums1, nums2)

# Count pairs that sum to 7: (2,5), (2,5), (2,5)
print(fsp.count(7))  # Output: 3

# Add 2 to nums2[2] => nums2 becomes [1, 2, 5, 4, 5]
fsp.add(2, 2)

# Now count pairs that sum to 8: (2,6), (2,5+2), (2,5+2)
print(fsp.count(8))  # Output: 0
