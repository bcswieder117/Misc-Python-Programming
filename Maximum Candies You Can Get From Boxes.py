# Blaine Swieder
# June 2nd, 2025
# LeetCode Challenge: Maximum Candies You Can Get from Boxes

# You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:

# status[i] is 1 if the ith box is open and 0 if the ith box is closed,
# candies[i] is the number of candies in the ith box,
# keys[i] is a list of the labels of the boxes you can open after opening the ith box.
# containedBoxes[i] is a list of the boxes you found inside the ith box.
# You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.
# Return the maximum number of candies you can get following the rules above.

from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque()
        have_keys = set()
        have_boxes = set(initialBoxes)
        opened = set()
        total_candies = 0

        # Add initially open boxes to the queue
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        # BFS loop
        while queue:
            box = queue.popleft()
            if box in opened:
                continue

            opened.add(box)
            total_candies += candies[box]

            # Collect keys and check if we can now open previously locked boxes
            for key in keys[box]:
                if key not in have_keys:
                    have_keys.add(key)
                    if key in have_boxes and key not in opened:
                        queue.append(key)

            # Collect contained boxes and open if possible
            for new_box in containedBoxes[box]:
                if new_box not in have_boxes:
                    have_boxes.add(new_box)
                if status[new_box] == 1 or new_box in have_keys:
                    queue.append(new_box)

        return total_candies

# Example usage
if __name__ == "__main__":
    solution = Solution()
    status = [1, 0, 1, 0]
    candies = [7, 5, 4, 100]
    keys = [[], [], [1], []]
    containedBoxes = [[1, 2], [3], [], []]
    initialBoxes = [0]
    print(solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Output: 16
